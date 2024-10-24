import sqlite3

def create_table():
    conn = sqlite3.connect('cs2_skins.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cs2_skins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT,
        lowest_price TEXT,
        volume TEXT,
        median_price TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def store_price_data(item_name, price_data):
    conn = sqlite3.connect('cs2_skins.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO cs2_skins (item_name, lowest_price, volume, median_price)
    VALUES (?, ?, ?, ?)
    ''', (
        item_name, 
        price_data.get('lowest_price'), 
        price_data.get('volume'), 
        price_data.get('median_price')
    ))
    
    conn.commit()
    conn.close()
