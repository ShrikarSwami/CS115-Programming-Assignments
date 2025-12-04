# === CS 115 Lab 11 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 11 ===

class Item:
    """
    Constructs an Instance of item with the following attributes
    name: name of the item
    damage_points: how much to reduce enemy HP during an attack
    regeneration_points: healing points to apply to a character if this item is used
    damage_type: type of damage. Can be "viral" "physical" or "electrical"
    is_consumable: true if the item can only be used once
    """
    def __init__(self, name, damage_points, regeneration_points, damage_type, is_consumable):
        self.name = name 
        self.damage_points = damage_points
        self.regeneration_points = regeneration_points
        self.damage_type = damage_type
        self.is_consumable = is_consumable

    def __hash__(self):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return hash((self.name, self.damage_points, self.regeneration_points, self.damage_type, self.is_consumable))

    def __eq__(self, other):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        if not isinstance(other, Item):
            return False
        return (self.name == other.name and
            self.damage_points == other.damage_points and
            self.regeneration_points == other.regeneration_points and
            self.damage_type == other.damage_type and
            self.is_consumable == other.is_consumable)

def create_healer_inventory():
    """
    creates an inventory of items for a healer character

    Do not read entire function!!!! Use stack trace and
    the debugger to isolate any errors
    """
    inventory = {
        Item("bandage", 0, 5, "physical", True): 1,
        Item("small_potion", 0, 8, "viral", True) : 3,
        Item("herb", 0, 3, "physical", True): 5,
        Item("antidote", 0, 7, "viral", True):2,
        Item("mega_potion", 0, 20, "viral", True):4,
        Item("revive_leaf", 0, 15, "electrical", True):0, 
        Item("healing_crystal", 0, 30, "physical", False):1,
        Item("ointment", 0, 4, "physical", True):1,
        Item("ginger", 0, (10,), "physical", True):1,
        Item("nano_patch", 0, 6, "electrical", True):3,
        Item("bio_gel", 0, 9, "viral", True):5,
        Item("hydration_vial", 0, 12, "physical", True):3,
        Item("regen_orb", 0, 25, "electrical", False):2,
        Item("soothing_salve", 0, 11, "physical", True):1,
        Item("mending_scroll", 0, 14, "viral", True):4,
    }

    return inventory


def compute_total_regeneration_points_in_inventory(inventory):
    """
    Computes the total regeneration points for all Items in the inventory.
    """
    total = 0 # Initialize total regeneration points to zero
    for item, item_quantity in inventory.items(): # Iterate through each item and its quantity in the inventory
        total += item_quantity * item.regeneration_points # Multiply the item's regeneration points by its quantity and add to total
    return total # Return the total regeneration points

###### The rest of the functions are for loop practice, the second part ######

def num_halves_until_one(n):
    if n<=1: # Base case: if n is less than or equal to 1, return 0
        return 0 # No halves needed
    count = 0 # Initialize count of halvings
    while n>1: # Loop until n is reduced to 1 or less
        n = n // 2 # Halve n using integer division
        count += 1 # Increment the count of halvings
    return count

def accumulate_costs(lst):
    cumulative_costs = [] # Initialize an empty list to store cumulative costs
    total = 0 # Initialize total cost to zero
    for value in lst: # Iterate through each value in the input list
        total = total + value # Calculate the new total by adding the current value
        cumulative_costs.append(total) # Append the new total to the cumulative costs list
    return cumulative_costs # Return the list of cumulative costs

def accumulate_col_costs(grid, col):
    cumulative = [] # Initialize an empty list to store cumulative costs for the specified column
    total = 0 # Initialize total cost to zero
    for row in grid: # Iterate through each row in the grid
        value = row
        total += value[col] # Add the value at the specified column to the total
        cumulative.append(total) # Append the current total to the cumulative list
    return cumulative # Return the list of cumulative costs for the specified column

def count_shared_values(gridX, gridY):
    setX = set() # Initialize an empty set to store unique values from gridX
    for row in gridX: # Iterate through each row in gridX
        for value in row: # Iterate through each value in the row
            setX.add(value) # Add the value to the set
    SetY = set() # Initialize an empty set to store unique values from gridY
    for row in gridY: # Iterate through each row in gridY
        for value in row: # Iterate through each value in the row
            SetY.add(value) # Add the value to the set
    shared_values = setX.intersection(SetY) # Find the intersection of the two sets
    return len(shared_values) # Return the count of shared values

if __name__ == "__main__":
     pass
     # Uncomment the code below to reproduce the bug
     # inventory = create_healer_inventory()
     # total_regeneration_points = compute_total_regeneration_points_in_inventory(inventory)
     # print(total_regeneration_points)
     



