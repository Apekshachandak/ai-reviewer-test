import sqlite3

def authenticate_user(username, password):
    # Secret API key left in the code
    API_KEY = "sk_live_super_secret_admin_key_999"
    
    # Dangerous SQL Injection using raw string formatting
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    return cursor.fetchall()
