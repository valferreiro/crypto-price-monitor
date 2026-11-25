import requests

from src.config import config

BASE_URL = "https://api.coingecko.com/api/v3"

DEFAULT_COINS = ["bitcoin", "ethereum", "solana"]

# Sesión HTTP reutilizable
session = requests.Session()
session.headers.update({
    "Accept": "application/json",
})


def get_market_prices(
    coin_ids: list[str] | None = None,
    currency: str = "usd",
) -> list[dict]:
    """
    Obtiene los precios actuales de criptomonedas desde CoinGecko.

    Args:
        coin_ids: IDs de las criptomonedas en CoinGecko.
        currency: Moneda de referencia.

    Returns:
        Lista de diccionarios con información del mercado.
    """

    if not config.COINGECKO_API_KEY:
        raise ValueError(
            "No se encontró COINGECKO_API_KEY en el archivo .env"
        )

    if coin_ids is None:
        coin_ids = DEFAULT_COINS

    if not coin_ids:
        raise ValueError("La lista de coin_ids no puede estar vacía")

    endpoint = f"{BASE_URL}/coins/markets"

    headers = {
        "x-cg-demo-api-key": config.COINGECKO_API_KEY,
    }

    params = {
        "vs_currency": currency.lower(),
        "ids": ",".join(coin_ids),
        "order": "market_cap_desc",
        "per_page": len(coin_ids),
        "page": 1,
        "sparkline": "false",
        "price_change_percentage": "24h",
    }

    try:
        response = session.get(
            endpoint,
            headers=headers,
            params=params,
            timeout=15,
        )

        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            raise ValueError(  # noqa: TRY004
                "La respuesta de CoinGecko no tiene el formato esperado."
            )

        return data

    except requests.exceptions.Timeout as error:
        raise RuntimeError(
            "La conexión con CoinGecko agotó el tiempo de espera."
        ) from error

    except requests.exceptions.HTTPError as error:
        raise RuntimeError(
            f"CoinGecko respondió con un error HTTP: {error}"
        ) from error

    except requests.exceptions.RequestException as error:
        raise RuntimeError(
            f"No fue posible conectar con CoinGecko: {error}"
        ) from error