from src.services.price_collector import collect_prices


def main():
    print("\nRecopilando y normalizando precios...\n")

    prices = collect_prices()

    for coin in prices:
        print(f"ID: {coin['coin_id']}")
        print(f"Nombre: {coin['name']}")
        print(f"Símbolo: {coin['symbol']}")
        print(f"Precio: {coin['price']} {coin['currency'].upper()}")
        print(f"Capitalización: {coin['market_cap']}")
        print(f"Volumen: {coin['total_volume']}")
        print(f"Variación 24h: {coin['price_change_percentage_24h']}")
        print(f"Fecha de captura: {coin['recorded_at']}")
        print(f"Fuente: {coin['source']}")
        print("-" * 50)


if __name__ == "__main__":
    main()
