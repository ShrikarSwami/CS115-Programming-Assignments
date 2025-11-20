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

    def __lt__(self, other):
        # I want “less than” to just mean “has less health than the other character”
        return self.health_points < other.health_points


    def transfer_loot(self, loot): #This moves all items in the loot dict into the current characters inventory
        loot_keys=list(loot.keys()) #Get the keys of the loot dict as a list

        def _transfer(index): #Helper function to do the transfer recursively
            if index>= len(loot_keys): #Base case which checks if we are done transferring all items
                return
            item = loot_keys[index] #Get the current item to transfer
            quantity = loot_keys[index] #Get the quantity of the current item
            quantity = loot.get(item,0) #Get the quantity of the current item in loot
            if quantity>0: #If there is at least one of the item to transfer 
                self.inventory[item] = self.inventory.get(item,0)+quantity #Add the quantity to the current character's inventory
                loot[item]=0 #Set the quantity in loot to 0 since we transferred all of it
            _transfer(index+1) #Recursive call to transfer the next item
         
        _transfer(0) #Start the recursive transfer with index 0
    
    def perform_move(self, move):
        # Grab the item this character is trying to use
        item = move.item
        # If I do not have this item (or have zero), I do nothing
        if self.inventory.get(item, 0) <= 0:
            return
        # Figure out who I am hitting
        target = move.other_character
        # Normal damage, no special multiplier here
        damage = item.damage_points
        # Apply damage and healing
        target.health_points -= damage
        self.health_points += item.regeneration_points
        # If the item is consumable, I use one up
        if item.is_consumable:
            self.inventory[item] -= 1

    def get_next_move(self, other_characters):
        # If there is nobody to attack, I say I have no move
        if not other_characters:
            return None

        # Pick the character with the lowest health out of the list
        target = min(other_characters, key=lambda c: c.health_points)

        # Pick the strongest item I have by damage_points
        strongest_item = max(self.inventory.keys())

        # Wrap it up in a Move object and return it
        return Move(target, strongest_item)


    
    # TODO Add other methods here.

# TODO Add other classes here
class PlayableCharacter(Character):
    #This is a character controlled by the player
    def get_user_input(self, other_characters):
        """
        Prompts the user to select an item and a target character.
        Returns a Move object based on the user's choices.
        """
        print("Here is oyur inventory!:")
        print(self.inventory)
        print("here are the enemies!:")
        print(other_characters)
        item_name = input("Enter the name of the item you want to use: ")
        target_index = int(input("Enter enemey number: "))
        item = get_inventory_item_from_item_name(item_name, self.inventory)
        target = other_characters[target_index]
        return Move(target, item)
    
    def get_next_move(self, other_characters):
        # For the d character I actually want to ask the user
        return self.get_user_input(other_characters)



class Robot(Character):
    # Robot is just a character with a shock baton and special electrical damage

    def __init__(self, name, max_health_points):
        # Let Character set up name, health, and rusty axe
        super().__init__(name, max_health_points)

        # Now I create the shock baton item
        baton = Item("shock baton", 1, 0, "electrical", False)

        # And give myself one baton, added to whatever I already had
        self.inventory[baton] = self.inventory.get(baton, 0) + 1

    def perform_move(self, move):
        # Same basic logic as Character.perform_move, but with electrical boost

        item = move.item

        # If I do not actually have this item, I stop here
        if self.inventory.get(item, 0) <= 0:
            return

        target = move.other_character

        # Start with the base damage
        damage = item.damage_points

        # Robots do double damage when the item is electrical
        if item.damage_type == "electrical":
            damage *= 2

        # Apply the hit and any regeneration
        target.health_points -= damage
        self.health_points += item.regeneration_points

        # Use up the item if it gets consumed
        if item.is_consumable:
            self.inventory[item] = self.inventory.get(item, 0) - 1

    def get_next_move(self, other_characters):
        # If there is nobody to attack, I cannot make a move
        if not other_characters:
            return None

        # Robots always attack the first character in the list
        target = other_characters[0]

        # I still want to hit as hard as I can, so I pick my strongest item
        strongest_item = max(self.inventory.keys())

        # Wrap that choice into a Move and return it
        return Move(target, strongest_item)


class Zombie(Character):
    # Zombie is a character that loves brain grenades and viral damage

    def __init__(self, name, max_health_points):
        # Let Character handle the basic setup
        super().__init__(name, max_health_points)

        # Create a viral brain grenade item
        grenade = Item("brain grenade", 5, 0, "viral", True)

        # Give myself three grenades by default
        self.inventory[grenade] = self.inventory.get(grenade, 0) + 3

    def get_next_move(self, other_characters):
        # If there is nobody to attack, I cannot make a move
        if not other_characters:
            return None

        # Zombies always attack the first character in the list
        target = other_characters[0]

        # Use my strongest item
        strongest_item = max(self.inventory.keys())

        return Move(target, strongest_item)

    def perform_move(self, move):
        # Similar to Character.perform_move, but viral attacks get doubled

        item = move.item

        if self.inventory.get(item, 0) <= 0:
            return

        target = move.other_character
        damage = item.damage_points

        # Zombies do double damage when the item is viral
        if item.damage_type == "viral":
            damage *= 2

        target.health_points -= damage
        self.health_points += item.regeneration_points

        if item.is_consumable:
            self.inventory[item] = self.inventory.get(item, 0) - 1

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
    if main_character.health_points <= 0 or enemy_that_will_attack.health_points <= 0: #If either character is already defeated, do nothing
        return #Exit the function early

    move = main_character.get_next_move(enemies) #Get the main character's move
    if move is None: #If no move is returned, do nothing
        return #Exit the function early
    main_character.perform_move(move) #Perform the move
    target = move.other_character #Get the target of the move so we can check its health

    if target.health_points <= 0: #If the target is defeated, transfer its loot to the main character
        main_character.transfer_loot(target.inventory) #Then transfer the loot
    else: #If the target is not defeated, the enemy attacks back
        enemy_move = enemy_that_will_attack.get_next_move([main_character]) #Get the enemy's move
        if enemy_move is None: #If no move is returned, do nothing
            return  #Exit the function early
        enemy_that_will_attack.perform_move(enemy_move) #Perform the enemy's move
        if main_character.health_points <= 0: #If the main character is defeated, transfer its loot to the enemy
            enemy_that_will_attack.transfer_loot(main_character.inventory) #Then transfer the loot


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


