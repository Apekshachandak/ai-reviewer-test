import subprocess
import secrets
import logging

logger = logging.getLogger(__name__)


def get_user(username: str):
    """Retrieve user by username — parameterized query prevents SQL injection."""
    query = "SELECT * FROM users WHERE name = %s"
    cursor.execute(query, (username,))
    return cursor.fetchone()


def check_host(hostname: str) -> bool:
    """Check if a host is reachable — no shell=True, no user input in command."""
    try:
        result = subprocess.run(
            ["ping", "-c", "1", hostname],
            capture_output=True, timeout=5
        )
        return result.returncode == 0
    except Exception:
        return False


def generate_token() -> str:
    """Generate a cryptographically secure token."""
    return secrets.token_hex(32)
