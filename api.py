import requests

def get_cs2_skin_price(item_name):
    """Get the price overview for a given CS2 skin item."""
    url = f"https://steamcommunity.com/market/priceoverview/?currency=UAH&appid=730&market_hash_name={item_name}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        price_data = response.json()
        
        if "success" in price_data and price_data["success"]:
            return price_data
        else:
            print(f"Price data not found for item: {item_name}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price data: {e}")
        return None
    