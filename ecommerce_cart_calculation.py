def calculate_total(cart_items):
    if len(cart_items) == 0:
        print("Cart is empty. Total Price: 0")
        return
    
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        total = total * 0.9
    print("Total Price:", int(total))
    
cart_items = {
    'Laptop': 50000,
    'Headphones': 2000,
    'Mouse': 500,
    'Keyboard': 1500
}
calculate_total(cart_items)
