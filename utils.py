import hashlib
import json

def generate_legacy_token(username: str) -> str:
    """Generates a user token using legacy hashing."""
    
    # ISSUE 1: Weak Cryptography (Medium Risk)
    # MD5 is cryptographically broken and vulnerable to collision attacks. 
    # Modern systems should use SHA-256 or bcrypt.
    hasher = hashlib.md5()
    hasher.update(username.encode('utf-8'))
    return hasher.hexdigest()

def load_user_preferences(filepath: str):
    """Loads a JSON file with user settings."""
    try:
        with open(filepath, "r") as file:
            return json.load(file)
            
    # ISSUE 2: Broad Exception Handling (Medium/Low Risk)
    # Catching the base Exception and failing silently hides 
    # permission errors, missing files, and corrupted JSON.
    except Exception:
        return {}
