import time
from api import get_cs2_skin_price
from database import create_table, store_price_data
from skins import skins  # Import the skin names from skins.py

def main():
    create_table()  # Ensure the table exists

    for item in skins:
        price_data = get_cs2_skin_price(item)
        if price_data:
            print("viewed skin")
            store_price_data(item, price_data)
        time.sleep(1)  # Add a 1-second delay between requests

if __name__ == "__main__":
    main()
