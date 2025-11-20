import random
# === CS 115 Homework 5 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:
#
# Pledge:
#
# === CS 115 Homework 5 ===

class Item:
    """
    This represents an in game item that can either deal damage or regenerate health.
    """
    # TODO Define constructor here
    #The todo just creates the items with all the required properties
    def __init__(self, name, damage_points, regeneration_points, damage_type, is_consumable):
        self.name = name
        self.damage_points = damage_points
        self.regeneration_points = regeneration_points
        self.damage_type = damage_type
        self.is_consumable = is_consumable

    def __str__(self):
        #Returns a short human readable description of the item.
        return f"Name: {self.name}, Damage: {self.damage_points}, Regen: {self.regeneration_points}"

    def __lt__(self, other):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return self.damage_points < other.damage_points

    def __hash__(self):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return hash((self.name, self.damage_points, self.regeneration_points, self.damage_type, self.is_consumable))

    def __repr__(self):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return str(self)

    def __eq__(self, other):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        if not isinstance(other, Item):
            return False
        return (self.name == other.name and
            self.damage_points == other.damage_points and
            self.regeneration_points == other.regeneration_points and
            self.damage_type == other.damage_type and
            self.is_consumable == other.is_consumable)

class Move:
    """
    Represents an action a character takes in a turn.
    """

    def __init__(self, other_character, item):
        self.other_character = other_character
        self.item = item

    def __str__(self):
        """ pretty prints Move. Do not change, but you can use as an example """
        return "Move: " + "\r\n" + "    Item: " + str(self.item) + "\r\n" + "    Target character: " + str(self.other_character)

#-----------------------------------------------------------------------------------------------------------------------------------
class Character:
    def __init__(self, name, max_health_points):
        self.name = name
        self.health_points = max_health_points
        self.inventory = {}
        rusty_axe = Item("rusty axe", 1, 0, "physical", False)
        self.inventory[rusty_axe] = 1

    def __str__(self): #This just represents the character and their health
        return f"{self.name} ({self.health_points} HP)"

    def __lt__(self, loot): #This represents the characters by their remaining health
        loot_keys = list(loot.keys())

    def transfer_loot(self, loot): #This moves all items in the loot dict into the current characters inventory
        loot_keys=list(loot.keys())

        def _transfer(index):
            if index>= len

    def get_next_move(self, other_characters):
        """Returns a Move targeting the character with lowest HP using strongest item."""
        pass  # TODO remove this line and implement
    # TODO Add other methods here.

# TODO Add other classes here








#----------------------------------------------------------------------------------------------------------------------------------

def spawn_enemies():
    """
    returns enemies based on what has already been implemented

    change this to include any characters you have implemented!
    """
    cubebot_1 = Character("little cubebot", 1)
    cubebot_2 = Character("armor cube", 2)
    return [cubebot_1, cubebot_2]

def standard_battle(main_character, enemies, enemy_that_will_attack):
    """
    Executes one round of combat between the player and a chosen enemy.

    Steps:
    1. The main_character selects a move using get_next_move(enemies).
    2. The main_character applies that move to its chosen target.
    3. If the target's health points reach 0, the main_character transfers
       all items from that target's inventory.
    4. Otherwise, enemy_that_will_attack selects a move using
       get_next_move([main_character]) and applies it.
    5. If the main_character's health points reach 0, the attacking enemy
       transfers all items from the main_character's inventory.
    """
    pass


def main_game_loop():
    """
    Do not change. If you would like a different game loop, implement
    one and call it custom_main_game_loop
    """
    main_character = PlayableCharacter("player", 15)
    enemies = spawn_enemies()
    while True:
        print("Main character info: " + str(main_character))
        enemies = [e for e in enemies if e.health_points > 0]
        if not enemies:
            print("You win!")
            break

        enemy = random.choice(enemies)
        standard_battle(main_character, enemies, enemy)
        print(f"Your stats: {main_character}")

        if main_character.health_points <= 0:
            print("You were defeated!")
            break

def get_inventory_item_from_item_name(item_name, inventory):
    """
    Helper function that might make get_next_move for PlayableCharacter easier
    Returns the Item object from inventory (dict with Item keys)
    whose name matches item_name, or None if not found.
    Assumes there will be just one matching item_name in the
    inventory, or will just match the first
    """
    name_matches = filter(lambda item: item.name == item_name, map(lambda i: i, inventory))
    return next(name_matches, None)


if __name__ == "__main__":
     pass
     # Change any code below to test or run your code
     # other_characters = spawn_enemies()
     # me = PlayableCharacter("alex", 5) #example test code
     # next_move = me.get_next_move(other_characters)
     # print(next_move)
     # main_game_loop() # uncomment this to start a game with the staff framework


