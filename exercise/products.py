products = [
    {"name": "Laptop", "price": 50000, "quantity": 2},
    {"name": "Mouse", "price": 500, "quantity": 5},
    {"name": "Keyboard", "price": 1200, "quantity": 3},
]

def price_calculator(products):
    grand_total = 0;

    for product in products:

        price = product['price'];
        quantity = product['quantity']

        item_total = price * quantity;
        
        if quantity > 3 :
            item_total -= item_total * 0.10

        grand_total += item_total

        print(f"{product['name']}: {item_total}");
    print (f"Total: {grand_total}")


price_calculator(products);


