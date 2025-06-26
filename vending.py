# Build a program that:
# Displays a list of snacks and drinks with item numbers and prices.
# Asks the user to choose items by number in a loop.
# Keeps track of selected items and their prices.
# Ends when the user types “done”.
# Finally prints a receipt showing:
# List of selected items with prices
# Total cost
"snacks" and "drinks" 
menu = {
         1: {"name": "chips", "price": 1.50},
         2: {"name": "pretizels", "price": 1.30},
         3: {"name": "cookies", "price": 3.00},
         4: {"name": "soda", "price": 1.75},
         5: {"name": "water bottle": 2.00}
print("Snack & Drink Menu:")
for number, item in menu.items():
    print(f"{number}. {item['name']} - ${item['price']:.2f}")
