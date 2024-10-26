import requests
import time

def get_cs2_skin_price(item_name):
    url = f"https://steamcommunity.com/market/priceoverview/?currency=USD&appid=730&market_hash_name={item_name}"
    retries = 3  # Number of times to retry the request

    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)  # Increase to 10 seconds

            response.raise_for_status()  # Raise an HTTPError for bad responses
            price_data = response.json()

            if "success" in price_data and price_data["success"]:
                return price_data
            else:
                print(f"Price data not found for item: {item_name}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error fetching price data (attempt {i+1}/{retries}): {e}")
            time.sleep(2)  # Wait for 2 seconds before retrying

    return None
