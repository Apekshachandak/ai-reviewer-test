# 1. SQL Injection 
import subprocess

def get_user(username):
    """Retrieve user by username using a parameterized query."""
    query = "SELECT * FROM users WHERE name = %s"
    cursor.execute(query, (username,))
    return cursor.fetchone()

def check_host(hostname):
    """Check if a host is reachable."""
    result = subprocess.run(
        ["ping", "-c", "1", hostname],
        capture_output=True, timeout=5
    )
    return result.returncode == 0


# 3. Weak Crypto 
def store_password(password):
    #testing
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()

# 4. Safe code 
def add_numbers(a, b):
    #testing
    return a + b
