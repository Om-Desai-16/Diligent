import sqlite3

conn = sqlite3.connect("ecom.db")
cur = conn.cursor()

query = """
SELECT 
    c.name,
    o.order_id,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS item_total,
    pay.payment_method,
    pay.payment_status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id
LEFT JOIN payments pay ON pay.order_id = o.order_id
LIMIT 10;
"""

for row in cur.execute(query):
    print(row)

conn.close()
