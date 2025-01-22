# List of products
products = [
    {"name": "Teddy Bear", "price": 25.99},  # Object located at Index 0
    {"name": "Hugs", "price": 0},
    {"name": "Chocolate", "price": 15.99},
    {"name": "Valentine's Day Card", "price": 2.99},
    {"name": "Dinner", "price": 79.99},
    {"name": "Flowers", "price": 12.99}
]

# Initialize an empty cart
cart = []

# Function to calculate the total price of items in the cart
def calculate_total_price(cart):
    total = sum(item["price"] for item in cart)
    return total

# Function to add an item to the cart
def add_to_cart(product_name):
    for product in products:
        if product["name"] == product_name:
            cart.append(product)
            print(f"{product_name} has been added to the cart.")
            break

# Function to calculate the final price with 12% tax
def result(total):
    tax = total * 0.12
    final_price = total + tax
    return final_price

# Example usage
add_to_cart("Teddy Bear")
add_to_cart("Chocolate")
add_to_cart("Flowers")

# Calculate the total price of items in the cart
total = calculate_total_price(cart)

# Display the cart items
print("\nCart:", [item["name"] for item in cart])

# Calculate and display the final price
final_price = result(total)
print(f"\nHere is the Final Price: {final_price:.2f}")
