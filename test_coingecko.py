
from src.api.coingecko import get_market_prices


def main():
    print("\nConsultando precios en CoinGecko...\n")

    prices = get_market_prices()

    for coin in prices:
        print(f"Criptomoneda: {coin['name']}")
        print(f"Símbolo: {coin['symbol'].upper()}")
        print(f"Precio: ${coin['current_price']:,.2f} USD")
        print(f"Capitalización: ${coin['market_cap']:,.2f}")
        print("-" * 40)


if __name__ == "__main__":
    main()
