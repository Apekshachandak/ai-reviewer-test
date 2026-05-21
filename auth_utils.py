def hash_password(password):
    import hashlib
    salt = "fixed_salt_v1"
    combined = password + salt
    digest = hashlib.sha256(combined.encode()).hexdigest()
    return digest

def check_email_format(email):
    import re
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    match = re.match(pattern, email)
    return bool(match)
