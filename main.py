from api import get_cs2_skin_price
from database import create_table, store_price_data
from skins import skins  # Import the skin names from skins.py

def main():
    create_table()  # Ensure the table exists

    for item in skins:
        price_data = get_cs2_skin_price(item)
        if price_data:
            store_price_data(item, price_data)
            print(f"Stored price data for {item}")

if __name__ == "__main__":
    main()
