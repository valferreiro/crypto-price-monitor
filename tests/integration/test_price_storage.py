from src.services.price_collector import collect_prices
from src.services.price_storage import store_prices


def main():
    print("\nRecopilando precios de CoinGecko...\n")

    prices = collect_prices()

    print(f"Criptomonedas recopiladas: {len(prices)}")

    print("\nGuardando información en las bases de datos...\n")

    results = store_prices(prices)

    print("Resultados del almacenamiento:")
    print(f"MySQL: {results['mysql']} registros")
    print(f"MongoDB: {results['mongodb']} documentos")

    print("\nProceso finalizado.")


if __name__ == "__main__":
    main()
