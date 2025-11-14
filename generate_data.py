#!/usr/bin/env python3
"""
generate_data.py
Generates 5 synthetic e-commerce CSV files in ./data
No external dependencies (uses only stdlib).
"""
import csv
import random
from datetime import datetime, timedelta
import os

random.seed(42)

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

NUM_CUSTOMERS = 60
NUM_PRODUCTS = 30
NUM_ORDERS = 120

# Helper functions
def rand_date_within(days_back=365):
    base = datetime.now()
    delta = timedelta(days=random.randint(0, days_back), hours=random.randint(0,23), minutes=random.randint(0,59))
    return (base - delta).strftime("%Y-%m-%d %H:%M:%S")

first_names = ["Alex","Sam","Priya","Ravi","Maya","John","Sara","Nina","Arjun","Leah","Isha","Vikram","Omar","Zara","Liam","Noah","Emma","Olivia","Ava","Lucas"]
last_names = ["Patel","Shah","Singh","Kumar","Smith","Johnson","Garcia","Khan","Das","Mehta","Thomas","Lee","Wong","Fernandez"]

def random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_email(name, idx):
    base = name.lower().replace(" ", ".")
    return f"{base}{idx}@example.com"

def random_phone():
    return f"+91{random.randint(6000000000,9999999999)}"

# 1) customers.csv
customers = []
for i in range(1, NUM_CUSTOMERS + 1):
    name = random_name()
    customers.append({
        "customer_id": i,
        "name": name,
        "email": random_email(name, i),
        "phone": random_phone(),
        "created_at": rand_date_within(1200)
    })

with open(os.path.join(DATA_DIR, "customers.csv"), "w", newline='', encoding='utf8') as f:
    writer = csv.DictWriter(f, fieldnames=["customer_id","name","email","phone","created_at"])
    writer.writeheader()
    writer.writerows(customers)

# 2) products.csv
categories = ["Books","Electronics","Kitchen","Clothing","Toys","Beauty","Sports"]
products = []
for i in range(1, NUM_PRODUCTS + 1):
    prod = {
        "product_id": i,
        "product_name": f"Product {i}",
        "category": random.choice(categories),
        "price": f"{random.choice([99,149,199,249,299,349,399,499,599,799])}"
    }
    products.append(prod)

with open(os.path.join(DATA_DIR, "products.csv"), "w", newline='', encoding='utf8') as f:
    writer = csv.DictWriter(f, fieldnames=["product_id","product_name","category","price"])
    writer.writeheader()
    writer.writerows(products)

# 3) orders & 4) order_items
orders = []
order_items = []
item_id = 1
for order_id in range(1, NUM_ORDERS + 1):
    cust = random.choice(customers)
    order_date = rand_date_within(365)
    # decide 1-4 items per order
    n_items = random.randint(1,4)
    total_amount = 0.0
    for _ in range(n_items):
        prod = random.choice(products)
        qty = random.randint(1,5)
        unit_price = float(prod["price"])
        line_total = qty * unit_price
        order_items.append({
            "item_id": item_id,
            "order_id": order_id,
            "product_id": prod["product_id"],
            "quantity": qty,
            "unit_price": f"{unit_price:.2f}"
        })
        item_id += 1
        total_amount += line_total
    orders.append({
        "order_id": order_id,
        "customer_id": cust["customer_id"],
        "order_date": order_date,
        "total_amount": f"{total_amount:.2f}"
    })

with open(os.path.join(DATA_DIR, "orders.csv"), "w", newline='', encoding='utf8') as f:
    writer = csv.DictWriter(f, fieldnames=["order_id","customer_id","order_date","total_amount"])
    writer.writeheader()
    writer.writerows(orders)

with open(os.path.join(DATA_DIR, "order_items.csv"), "w", newline='', encoding='utf8') as f:
    writer = csv.DictWriter(f, fieldnames=["item_id","order_id","product_id","quantity","unit_price"])
    writer.writeheader()
    writer.writerows(order_items)

# 5) payments.csv
payments = []
methods = ["card", "upi", "netbanking", "cod"]
statuses = ["paid","failed","pending"]
for o in orders:
    pay_date = datetime.strptime(o["order_date"], "%Y-%m-%d %H:%M:%S") + timedelta(hours=random.randint(1,72))
    payments.append({
        "payment_id": o["order_id"],  # one payment per order (simple)
        "order_id": o["order_id"],
        "payment_method": random.choice(methods),
        "payment_status": random.choices(["paid","failed","pending"], weights=[0.8,0.05,0.15])[0],
        "payment_date": pay_date.strftime("%Y-%m-%d %H:%M:%S")
    })

with open(os.path.join(DATA_DIR, "payments.csv"), "w", newline='', encoding='utf8') as f:
    writer = csv.DictWriter(f, fieldnames=["payment_id","order_id","payment_method","payment_status","payment_date"])
    writer.writeheader()
    writer.writerows(payments)

print("Generated CSV files in ./data/")
