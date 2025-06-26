def display_menu(menu_categories):
    """Displays the menu with numbered items and their prices."""
    print("\n--- Our Menu ---")
    all_items = []
    item_number = 1
    for category, items in menu_categories.items():
        print(f"\n--- {category} ---")
        for item_name, price in items.items():
            print(f"{item_number}. {item_name: <15} ${price:.2f}")
            all_items.append((item_name, price)) # Store (name, price) tuple for selection
            item_number += 1
    print("----------------")
    return all_items # Return the flat list of (item, price) tuples

def get_user_choice(max_item_number):
    """Gets a valid item number or 'done' from the user."""
    while True:
        user_input = input("Enter the number of your desired item (or 'done' to finish): ").strip().lower()
        
        if user_input == "done":
            return "done"
        
        try:
            choice = int(user_input)
            if 1 <= choice <= max_item_number:
                return choice
            else:
                print(f"Invalid number. Please choose a number between 1 and {max_item_number}.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

def main():
    """Main function to run the snack and drink selection with prices and receipt."""
    menu = {
        "Snacks": {
            "Chips": 1.50,
            "Cookies": 2.00,
            "Pretzels": 1.25,
            "Fruit Bar": 2.50,
            "Granola Bar": 1.754
        },
        "Drinks": {
            "Water": 1.00,
            "Soda": 2.25,
            "Juice": 2.75,
            "Coffee": 3.00,
            "Tea": 2.50
        }
    }

    selected_items = [] # Stores (item_name, price) tuples for the order
    
    print("Welcome to our snack and drink selection!")
    print("Type 'done' at any time to finish your order.")

    # Get the flat list of all items with their prices from the menu
    # This list maps item numbers to (name, price) tuples
    numbered_menu_items = display_menu(menu)
    max_item_number = len(numbered_menu_items)

    while True:
        choice = get_user_choice(max_item_number)

        if choice == "done":
            break
        else:
            # Adjust for 0-based indexing since item numbers are 1-based
            chosen_item_name, chosen_item_price = numbered_menu_items[choice - 1]
            selected_items.append((chosen_item_name, chosen_item_price))
            print(f"You've added {chosen_item_name} (${chosen_item_price:.2f}) to your selection.")
            print("---") # Separator for clarity

    # --- Print Receipt ---
    if selected_items:
        print("\n" + "="*30)
        print(f"{'--- Your Receipt ---':^30}")
        print("="*30)
        
        total_cost = 0
        for item_name, price in selected_items:
            print(f"{item_name: <20} ${price:.2f}")
            total_cost += price
        
        print("-" * 30)
        print(f"{'Total:': <20} ${total_cost:.2f}")
        print("=" * 30)
        print("\nThank you for your order! Enjoy your selections!")
    else:
        print("\nYou didn't select any items. Come back soon!")

if __name__ == "__main__":
    main()