"""Data service for fetching and processing records."""
import sqlite3
import time


def get_all_users_with_orders():
    """Fetch all users and their orders."""
    conn = sqlite3.connect("/tmp/app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    result = []
    for user in users:
        # N+1: separate query for each user's orders
        cursor.execute(f"SELECT * FROM orders WHERE user_id = {user[0]}")
        orders = cursor.fetchall()
        result.append({"user": user, "orders": orders})
    conn.close()
    return result


def search_products(query: str):
    """Search products by name - no pagination."""
    conn = sqlite3.connect("/tmp/app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", (f"%{query}%",))
    products = cursor.fetchall()
    conn.close()
    return products


def get_expensive_report():
    """Generate an expensive report with no caching."""
    conn = sqlite3.connect("/tmp/app.db")
    cursor = conn.cursor()
    time.sleep(0.1)
    cursor.execute("""
        SELECT u.name, COUNT(o.id) as order_count, SUM(o.total) as total_spent
        FROM users u JOIN orders o ON u.id = o.user_id
        GROUP BY u.id ORDER BY total_spent DESC
    """)
    report = cursor.fetchall()
    conn.close()
    return report
