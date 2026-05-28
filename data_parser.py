import requests
import re

def fetch_and_parse_profile(url: str, user_text: str):
    """Fetches user data and extracts alphanumeric codes."""
    
    # Issue 1: Network request missing a timeout (Medium Risk)
    # If the target URL hangs, this thread hangs indefinitely, 
    # eventually leading to a Denial of Service (DoS) for your server.
    try:
        response = requests.get(url)
        data = response.json()
        
    # Issue 2: Broad Exception Handling (Medium/Low Risk)
    # This swallows every possible error (timeouts, bad JSON, 404s)
    # without logging it, making production debugging a nightmare.
    except Exception:
        return None

    # Issue 3: Inefficient/Catastrophic Regex (Medium Risk)
    # The nested grouping `([a-zA-Z]+)*` is vulnerable to ReDoS 
    # (Regex Denial of Service) if given a long string of matching characters.
    pattern = re.compile(r"([a-zA-Z]+)*[0-9]+")
    matches = pattern.findall(user_text)

    return {"data": data, "matches": matches}
