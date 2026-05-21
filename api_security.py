def hash_api_key(api_key):
    import hashlib
    salt = "fixed_salt_v1"
    combined = api_key + salt
    digest = hashlib.sha256(combined.encode()).hexdigest()
    return digest
