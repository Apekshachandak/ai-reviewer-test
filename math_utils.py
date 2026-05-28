def calculate_rectangle_area(length: float, width: float) -> float:
    """Safely calculates the area of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative.")
    
    return length * width

def format_greeting(name: str) -> str:
    """Returns a properly formatted greeting string."""
    if not name or not isinstance(name, str):
        return "Hello, Guest!"
        
    clean_name = name.strip().title()
    return f"Hello, {clean_name}!"
