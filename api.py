"""API module with intentional bugs for PR Rocket to find."""

import sqlite3

def get_user(user_id):
    """Fetch user from database."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # Bug: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    return cursor.fetchone()

def process_data(data):
    """Process user data."""
    if not data:
        return None
    # Bug: potential null dereference
    return data.name.lower()

def format_output(items, limit=10):
    """Format list of items."""
    result = []
    for i, item in enumerate(items):
        if i >= limit:
            break
        # Bug: no null check
        result.append(item.upper())
    return "\n".join(result)

def calculate_stats(numbers):
    """Calculate statistics."""
    total = sum(numbers)
    average = total / len(numbers)  # Bug: division by zero if empty
    return {"total": total, "avg": average}

class Config:
    """Configuration class."""
    def __init__(self):
        self._settings = {}
    
    def get(self, key, default=None):
        return self._settings.get(key, default)
    
    def set(self, key, value):
        self._settings[key] = value

def deprecated_function():
    """This function is deprecated."""
    pass
