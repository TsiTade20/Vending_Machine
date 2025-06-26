# --- 1. Define the Menu of Snacks and Drinks ---
# This dictionary holds all our items, organized by category (Snacks, Drinks).
# Each item has a name and a price.
MENU_ITEMS = {
    "Snacks": {
        "Chips": 1.50,
        "Cookies": 2.00,
        "Pretzels": 1.25,
        "Fruit Bar": 2.50,
        "Granola Bar": 1.75
    },
    "Drinks": {
        "Water": 1.00,
        "Soda": 2.25,
        "Juice": 2.75,
        "Coffee": 3.00,
        "Tea": 2.50
    }
}

def display_and_map_menu(menu_data):
    """
    Displays the menu to the user with numbers and prices.
    Also creates a 'lookup map' so we can easily find an item by its number.
    
    Args:
        menu_data (dict): The dictionary containing all menu items and their prices.

    Returns:
        tuple: A tuple containing:
            - dict: A dictionary mapping item numbers (int) to (item_name, price) tuples.
            - int: The highest item number displayed.
    """
    print("\n--- Our Available Items ---")
    
    # This dictionary will store our item number to (name, price) mappings.
    # Example: {1: ("Chips", 1.50), 2: ("Cookies", 2.00), ...}
    item_number_to_details_map = {} 
    current_item_number = 1 # Start numbering items from 1

    # Loop through each category (like "Snacks" or "Drinks") in our menu
    for category_name, items_in_category in menu_data.items():
        print(f"\n--- {category_name} ---")
        
        # Loop through each individual item within the current category
        for item_name, item_price in items_in_category.items():
            # Print the item number, its name, and its price, nicely formatted
            print(f"{current_item_number}. {item_name: <15} ${item_price:.2f}")
            
            # Store this item's details in our lookup map
            item_number_to_details_map[current_item_number] = (item_name, item_price)
            
            # Move to the next item number
            current_item_number += 1
            
    print("-------------------------")
    
    # Return the map and the last item number used
    return item_number_to_details_map, current_item_number - 1 # current_item_number is one higher than max

def get_user_order_choice(highest_item_number):
    """
    Asks the user for their choice (an item number or 'done').
    Validates the input to ensure it's a valid number or 'done'.
    
    Args:
        highest_item_number (int): The largest valid item number the user can choose.

    Returns:
        Union[int, str]: The valid item number (as an int) or the string "done".
    """
    while True:
        user_input = input(
            f"Enter the number of an item to add, or type 'done' to finish: "
        ).strip().lower() # .strip() removes spaces, .lower() makes it lowercase

        # Check if the user wants to finish
        if user_input == "done":
            return "done"
        
        # Try to convert the input to a number
        try:
            chosen_number = int(user_input)
            
            # Check if the number is within our valid range
            if 1 <= chosen_number <= highest_item_number:
                return chosen_number # It's a valid item number!
            else:
                print(f"Oops! Please enter a number between 1 and {highest_item_number}.")
        except ValueError:
            # This happens if the user types something that isn't a number or "done"
            print("That's not a valid input. Please enter a number or 'done'.")

def print_receipt(items_bought):
    """
    Prints a detailed receipt for the customer.
    
    Args:
        items_bought (list): A list of (item_name, item_price) tuples
                             representing what the user selected.
    """
    if not items_bought: # If the list is empty, nothing was bought
        print("\nYou didn't select any items. Maybe next time!")
        return

    print("\n" + "="*35) # Top border for the receipt
    print(f"{'--- Your Receipt ---':^35}") # Centered title
    print("="*35)
    
    total_bill_amount = 0.0 # Start our total at zero

    # Loop through each item the user selected
    for item_name, item_price in items_bought:
        # Print the item name and its price, nicely aligned
        print(f"{item_name: <25} ${item_price:.2f}")
        total_bill_amount += item_price # Add this item's price to the total
    
    print("-" * 35) # Separator line
    # Print the final total amount
    print(f"{'Total to Pay:': <25} ${total_bill_amount:.2f}")
    print("=" * 35) # Bottom border
    print("\nThank you for your purchase! Enjoy!")


# --- Main Program Logic ---
def run_snack_machine():
    """
    This is the main function that runs our snack and drink ordering program.
    """
    print("Welcome to our online snack and drink machine!")
    print("You can select multiple items. Type 'done' when you are finished ordering.")

    # Step 1: Display the menu and get our number-to-item mapping
    # item_lookup_map will be like {1: ("Chips", 1.50), 2: ("Cookies", 2.00), ...}
    # max_item_number will be the largest number displayed (e.g., 10)
    item_lookup_map, max_item_number = display_and_map_menu(MENU_ITEMS)
    
    # This list will store all the items the user chooses
    customer_selected_items = [] 

    # Step 2: Loop to get user choices until they type 'done'
    while True:
        # Ask the user for their next choice
        user_choice = get_user_order_choice(max_item_number)

        # If the user typed 'done', we stop the loop
        if user_choice == "done":
            break 
        else:
            # If they entered a number, get the item details from our map
            chosen_item_name, chosen_item_price = item_lookup_map[user_choice]
            
            # Add the chosen item (name and price) to our list of selected items
            customer_selected_items.append((chosen_item_name, chosen_item_price))
            
            print(f"Added: {chosen_item_name} (${chosen_item_price:.2f})")
            print("---") # A little separator for readability in the console

    # Step 3: Print the final receipt
    print_receipt(customer_selected_items)

# This line makes sure run_snack_machine() only runs when the script is executed directly.
if __name__ == "__main__":
    run_snack_machine()