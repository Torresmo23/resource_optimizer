import sqlite3

def create_table():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS inventory
                 (item TEXT, price REAL, max_qty INTEGER)''')
    conn.commit()
    conn.close()

def insert_item(item, price, max_qty):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO inventory VALUES (?, ?, ?)", (item, price, max_qty))
    conn.commit()
    conn.close()

def fetch_items():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM inventory")
    data = c.fetchall()
    conn.close()
    return data