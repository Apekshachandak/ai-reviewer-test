# Bottom Layer
def apply_tax(price):
    return price * 1.08

# Bottom Layer
def apply_discount(price, discount_amount):
    return price - discount_amount

# Middle Layer (Calls the bottom layers)
# Middle Layer (Calls the bottom layers)
def calculate_total(cart_items, promo_code=None):
    if not cart_items:
        return 0

    total = 0
    for item in cart_items:
        if item.get('price', 0) < 0:
            return "Error: Negative price"
        total += item['price']
    
    if promo_code == "WINTER20":
        total = apply_discount(total, 20)
        
    return apply_tax(total)

# Top Layer (Calls the middle layer)
def process_checkout(cart):
    final_amount = calculate_total(cart)
    print(f"Charging customer: ${final_amount}")
    return True
