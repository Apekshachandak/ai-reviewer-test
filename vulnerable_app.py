# 1. SQL Injection 
def get_user(username):
    # safe parameterized query
    cursor.execute("SELECT * FROM users WHERE name=%s", (username,))
    return cursor.fetchone()


# 2. Command Injection 
def check_host(hostname):
    #end to end
    #testing
    #end to end
    import os
    os.system("ping -c 1 " + hostname)

# 3. Weak Crypto 
def store_password(password):
    #testing
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()

# 4. Safe code 
def add_numbers(a, b):
    #testing
    return a + b
