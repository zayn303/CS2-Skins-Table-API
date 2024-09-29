import mysql.connector
import os
from dotenv import load_dotenv
from request import get_cs2_skin_price  # Ensure this file has the function defined
from skins import cs2_skins             # Ensure this file contains the list of skins

# Load environment variables from .env file
load_dotenv()

# Function to connect to MySQL
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to insert skin price data into the database
def insert_skin_price(skin_name, lowest_price, median_price, volume):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO cs2_skin_prices (skin_name, lowest_price, median_price, volume) VALUES (%s, %s, %s, %s)",
                (skin_name, lowest_price, median_price, volume)
            )
            connection.commit()  # Commit the transaction
            print(f"Inserted data for {skin_name}")
        except mysql.connector.Error as err:
            print(f"Failed inserting {skin_name}: {err}")
        finally:
            cursor.close()
            connection.close()

# Fetch prices for each skin and insert into database
def fetch_and_store_prices():
    for skin in cs2_skins:
        price_info = get_cs2_skin_price(skin)
        if price_info:
            lowest_price = float(price_info['lowest_price'].replace('$', '').replace(',', ''))  # Clean up price
            median_price = float(price_info['median_price'].replace('$', '').replace(',', ''))  # Clean up price
            volume = price_info['volume']  # Ensure volume is an integer
            
            # Insert the skin price data into the database
            insert_skin_price(skin, lowest_price, median_price, volume)
            print(f"Item: {skin}, Lowest Price: {lowest_price}, Median Price: {median_price}, Volume: {volume}")

if __name__ == "__main__":
    fetch_and_store_prices()
