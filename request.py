import requests

def get_cs2_skin_price(item_name):
    """Get the price overview for a given CS2 skin item."""
    # Replace spaces in item_name with %20 for the URL
    item_name_encoded = item_name.replace(" ", "%20")
    
    url = f"https://steamcommunity.com/market/priceoverview/?currency=USD&appid=730&market_hash_name={item_name_encoded}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse JSON response
        price_data = response.json()
        
        # Check if the item exists in the market
        if "success" in price_data and price_data["success"]:
            return price_data
        else:
            print(f"Price data not found for item: {item_name}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price data: {e}")
        return None
