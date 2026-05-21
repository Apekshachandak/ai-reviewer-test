def calculate_discount(price, discount):
    if price < 0:
        return 0
    return price - (price * discount)
