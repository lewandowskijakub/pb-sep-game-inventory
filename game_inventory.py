
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    for key, value in inventory.items():
        print(f"{key}: {value}")



def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    pass


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for item in removed_items:
        if item in inventory.keys() and inventory[item] > 1:
            inventory[item] -= 1
        elif item not in inventory:
            print(f"You can't remove {item} from inventory")
        else:
            del inventory[item]
    pass


def print_table(inventory, order):
    # Takes your inventory and displays it in a well-organized table with
    # each column right-justified. The input argument is an order parameter (string)
    # which works as the following:
    # - None (by default) means the table is unordered
    # - "count,desc" means the table is ordered by count (of items in the inventory)
    #   in descending order
    # - "count,asc" means the table is ordered by count in ascending order  
    if order == "count,asc":
        inventory = dict(sorted(inventory.items(), key=lambda x:x[1]))
    elif order == "count,desc":
        inventory = dict(sorted(inventory.items(), key=lambda x:x[1], reverse=True))
    
    print("-----------------")
    print("item name | count")
    print("-----------------")
    for key, value in inventory.items():
        print(key.rjust(9), str(value).rjust(6), sep=" |")
    print("-----------------")


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""
    with open(filename) as file:
        data = file.read()
        list_of_data = data.split(",")
        add_to_inventory(inventory, list_of_data)
    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass
