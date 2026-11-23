from datetime import datetime, timezone

from src.api.coingecko import get_market_prices


def normalize_market_data(
    market_data: list[dict],
    currency: str = "usd",
) -> list[dict]:
    """
    Normaliza los datos recibidos de CoinGecko.

    Cada registro representa una observación del precio
    de una criptomoneda en un momento determinado.
    """

    if not market_data:
        return []

    # Una misma fecha de captura para todos los registros.
    recorded_at = datetime.now(timezone.utc).replace(tzinfo=None)

    normalized_data = []

    for coin in market_data:

        required_fields = [
            "id",
            "symbol",
            "name",
            "current_price",
        ]

        if not all(field in coin for field in required_fields):
            raise ValueError(
                f"Faltan campos obligatorios en el registro: {coin}"
            )

        if coin["current_price"] is None:
            raise ValueError(
                f"El precio de {coin['name']} no está disponible."
            )

        normalized_coin = {
            "coin_id": coin["id"],
            "symbol": coin["symbol"].upper(),
            "name": coin["name"],
            "price": coin["current_price"],
            "currency": currency.lower(),
            "recorded_at": recorded_at,
            "source": "coingecko",
            "market_cap": coin.get("market_cap"),
            "total_volume": coin.get("total_volume"),
            "price_change_percentage_24h": coin.get(
                "price_change_percentage_24h"
            ),
        }

        normalized_data.append(normalized_coin)

    return normalized_data


def collect_prices(
    coin_ids: list[str] | None = None,
    currency: str = "usd",
) -> list[dict]:
    """
    Obtiene y normaliza los precios de las criptomonedas.
    """

    market_data = get_market_prices(
        coin_ids=coin_ids,
        currency=currency,
    )

    return normalize_market_data(
        market_data=market_data,
        currency=currency,
    )
