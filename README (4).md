
# 📦 E-Commerce Project Diligent
### *AI-Assisted Dataset Generation • SQLite Database Creation • Multi-Table SQL Querying*

This project demonstrates a complete **AI-Assisted Software Development Lifecycle (A-SDLC)** workflow using Cursor + Python.  
The system generates synthetic e-commerce data, ingests it into a SQLite database, and runs multi-table SQL analysis.

Included in this repository:

✔ Synthetic dataset (CSV files)  
✔ SQLite database (`ecom.db`)  
✔ Python scripts for data generation, ingestion, and analysis  
✔ SQL query used  
✔ Prompts used to generate the project  
✔ Commands to run everything  

---

# 📁 Directory Structure

ecom-demo/
├─ data/
│ ├─ customers.csv
│ ├─ products.csv
│ ├─ orders.csv
│ ├─ order_items.csv
│ └─ payments.csv
├─ ecom.db
├─ generate_data.py
├─ ingest_data.py
├─ run_query.py
├─ prompts.txt
├─ README.md


---

# 🧰 Requirements

No installations required:

- Python 3.8+
- SQLite (included automatically with Python)

---

# 🚀 How to Run the Project

### **1️⃣ Generate Synthetic Data**
This script creates 5 CSV files under `/data`.

```bash
python3 generate_data.py

python3 ingest_data.py

python3 run_query.py
```
### **Customers**
| Column      | Type    |
| ----------- | ------- |
| customer_id | INTEGER |
| name        | TEXT    |
| email       | TEXT    |
| phone       | TEXT    |
| created_at  | TEXT    |

### **Product**
| Column       | Type    |
| ------------ | ------- |
| product_id   | INTEGER |
| product_name | TEXT    |
| category     | TEXT    |
| price        | REAL    |

### **Order**
| Column       | Type    |
| ------------ | ------- |
| order_id     | INTEGER |
| customer_id  | INTEGER |
| order_date   | TEXT    |
| total_amount | REAL    |

### **Order_items**
| Column     | Type    |
| ---------- | ------- |
| item_id    | INTEGER |
| order_id   | INTEGER |
| product_id | INTEGER |
| quantity   | INTEGER |
| unit_price | REAL    |

### **payments**
| Column         | Type    |
| -------------- | ------- |
| payment_id     | INTEGER |
| order_id       | INTEGER |
| payment_method | TEXT    |
| payment_status | TEXT    |
| payment_date   | TEXT    |


### **Prompt 1 — Generate Synthetic Data**
Generate five synthetic e-commerce CSV files and save them in a /data folder:
customers.csv, products.csv, orders.csv, order_items.csv, payments.csv.
Ensure valid foreign key relationships and realistic sample values.

### **Prompt 2 — Ingest CSV Files into SQLite**
Write a Python script that:
- Creates a SQLite database file named ecom.db
- Creates tables: customers, products, orders, order_items, payments
- Loads all CSV files from ./data into the database
- Prints confirmation messages for each table loaded
Use only Python's built-in sqlite3 and csv modules.

### **Prompt 3 — SQL JOIN Query**

Write a SQL query that joins customers, orders, order_items, products, and payments.
Return customer name, order ID, order date, product name, quantity, unit price, item total, payment method, payment status, and total order amount.
Also write a Python script run_query.py that connects to ecom.db and prints the first 10 rows.
