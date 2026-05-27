"""
safe_utils.py — Utility functions using secure coding practices.
"""

import hashlib
import secrets


def greet_user(name: str) -> str:
    """Return a greeting message for the given name."""
    if not isinstance(name, str) or not name.strip():
        return "Hello, Guest!"
    safe_name = name.strip()[:50]  # limit length
    return f"Hello, {safe_name}!"


def hash_password(password: str) -> str:
    """Hash a password using SHA-256 with a random salt."""
    salt = secrets.token_hex(16)
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{hashed}"


def verify_password(password: str, stored_hash: str) -> bool:
    """Verify a password against its stored hash."""
    try:
        salt, expected = stored_hash.split(":", 1)
        actual = hashlib.sha256((salt + password).encode()).hexdigest()
        return secrets.compare_digest(actual, expected)
    except ValueError:
        return False


def calculate_discount(price: float, percent: float) -> float:
    """Calculate discounted price. Validates inputs before computing."""
    if not (0 <= percent <= 100):
        raise ValueError("Discount percent must be between 0 and 100")
    if price < 0:
        raise ValueError("Price cannot be negative")
    return round(price * (1 - percent / 100), 2)
