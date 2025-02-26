import sqlite3
import requests

urlSales = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=760830694&single=true&output=csv"
urlProducts = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=0&single=true&output=csv"
urlStores = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=714623615&single=true&output=csv"

responseSales = requests.get(urlSales)
responseProducts = requests.get(urlProducts)
responseStores = requests.get(urlStores)

print(responseSales)
print(responseProducts)
print(responseStores)

connection = sqlite3.connect('data/sales.db')

cursor = connection.cursor()

create_table_products = """CREATE TABLE IF NOT EXISTS
products(id INTEGER PRIMARY KEY, name VARCHAR(100), price DECIMAL(10,2), stock INTEGER)"""


create_table_stores = """CREATE TABLE IF NOT EXISTS
stores(id INTEGER PRIMARY KEY, city VARCHAR(100), number_of_employees INTEGER)"""


create_table_sales = """CREATE TABLE IF NOT EXISTS
sales(id INTEGER PRIMARY KEY,
    date DATE,
    quantity INTEGER,
    product_id INTEGER,
    store_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (store_id) REFERENCES stores(id))"""


create_table_total_revenue = """CREATE TABLE IF NOT EXISTS
total_revenue(id INTEGER PRIMARY KEY,
    product_id INTEGER,
    store_id INTEGER,
    total_revenue_amount DECIMAL(10, 2),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (store_id) REFERENCES stores(id))"""

create_table_sales_per_store = """CREATE TABLE IF NOT EXISTS
sales_per_store(id INTEGER PRIMARY KEY, quantity_sold INTEGER, revenue_per_store DECIMAL(10,2), store_id INTEGER, FOREIGN KEY (store_id) REFERENCES stores(id))"""

create_table_sales_per_product = """CREATE TABLE IF NOT EXISTS
sales_per_product(id INTEGER PRIMARY KEY, quantity_sold INTEGER, revenue_per_product DECIMAL(10,2), product_id INTEGER, FOREIGN KEY (product_id) REFERENCES products(id))"""

# cursor.execute(create_table_products)
# cursor.execute(create_table_stores)
# cursor.execute(create_table_sales)
# cursor.execute(create_table_total_revenue)
# cursor.execute(create_table_sales_per_store)
# cursor.execute(create_table_sales_per_product)

connection.commit()
connection.close()