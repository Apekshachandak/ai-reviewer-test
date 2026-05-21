# Function C (The bottom layer)
def save_to_database(data):
    if not data:
        return False
    print("Saved!")
    return True

# Function B (The middle layer)
def register_user(username, age, email=None):
    if age < 18:
        return "Too young"
    
    # WE ARE ADDING NEW COMPLEXITY HERE
    if email is not None:
        if "@" not in email:
            return "Invalid email"
    
    success = save_to_database(username)
    return success

# Function A (The top layer)
def api_endpoint(request_data):
    user = request_data.get("user")
    age = request_data.get("age")
    
    # Notice it calls the middle layer!
    if user and age:
        return register_user(user, age)
    return "Error"
