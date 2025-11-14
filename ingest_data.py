#!/usr/bin/env python3
"""
ingest_data.py
Creates ecom.db and loads CSVs into SQLite tables.
Uses only the standard library.
"""
import sqlite3
import csv
import os

DATA_DIR = "data"
DB_FILE = "ecom.db"

def create_tables(conn):
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        phone TEXT,
        created_at TEXT
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        category TEXT,
        price REAL
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT,
        total_amount REAL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        item_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        unit_price REAL,
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        payment_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        payment_method TEXT,
        payment_status TEXT,
        payment_date TEXT,
        FOREIGN KEY (order_id) REFERENCES orders(order_id)
    );
    """)
    conn.commit()

def load_csv_to_table(conn, csv_path, table_name, columns):
    with open(csv_path, newline='', encoding='utf8') as f:
        reader = csv.DictReader(f)
        rows = []
        for r in reader:
            rows.append([r[col] for col in columns])
    placeholders = ",".join(["?"] * len(columns))
    query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
    conn.executemany(query, rows)
    conn.commit()
    print(f"Loaded {len(rows)} rows into {table_name}")

def main():
    if not os.path.isdir(DATA_DIR):
        raise SystemExit("Run generate_data.py first to create ./data/ CSV files.")
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    conn = sqlite3.connect(DB_FILE)
    create_tables(conn)

    load_csv_to_table(conn, os.path.join(DATA_DIR, "customers.csv"), "customers",
                      ["customer_id","name","email","phone","created_at"])
    load_csv_to_table(conn, os.path.join(DATA_DIR, "products.csv"), "products",
                      ["product_id","product_name","category","price"])
    load_csv_to_table(conn, os.path.join(DATA_DIR, "orders.csv"), "orders",
                      ["order_id","customer_id","order_date","total_amount"])
    load_csv_to_table(conn, os.path.join(DATA_DIR, "order_items.csv"), "order_items",
                      ["item_id","order_id","product_id","quantity","unit_price"])
    load_csv_to_table(conn, os.path.join(DATA_DIR, "payments.csv"), "payments",
                      ["payment_id","order_id","payment_method","payment_status","payment_date"])

    conn.close()
    print(f"Database created: {DB_FILE}")

if __name__ == "__main__":
    main()
