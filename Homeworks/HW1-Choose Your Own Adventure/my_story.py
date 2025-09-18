"""
Choose Your Own Adventure: Morning Rush

"""


def get_user_input():
    """Ask the player for a single letter choice and return it in lowercase with spaces trimmed."""
    # I ask the user to type a single letter that represents their choice
    # I  use the exact prompt text that the assignment expects just because cmd c and v is easy!
    letter = input("Type in your action and press <Enter>: ")
    # I convert the answer to lowercase so that A and a are treated the same (Thanks BAnderson!)
    # I also trim surrounding spaces so stray spaces do not break the logic (Average Python reference)
    return letter.lower().strip()


def print_choices(choice1, choice2, choice3):
    """Print three labeled choices on separate lines using the exact a b c format."""
    # I show the three options in a tidy consistent format
    # Each choice appears on its own line
    print(f"a) {choice1}")
    print(f"b) {choice2}")
    print(f"c) {choice3}")


def get_valid_choice():
    """Repeat reading input until the player types a valid letter which is a or b or c."""
    # I keep asking for input until the user types a valid option
    while True:
        # I read a letter using the helper that already applies the required prompt and cleanup
        choice = get_user_input()
        # I accept only a or b or c per the assignment
        if choice in ("a", "b", "c"):
            # I return the valid letter to the caller
            return choice
        # I tell the user what went wrong and I loop to ask again
        print("Invalid choice. Please type a, b, or c.")


# -------------- Story scene functions --------------


def route_a():
    """Handle route a which is Sleep a little longer and end right away."""
    # I describe the outcome of sleeping longer
    print("You decided to sleep a little longer and you miss every class.")
    # I clearly state the consequence
    print("You are kicked out of Stevens.")
    # I mark the end of the game
    print("Game over.")


def route_b():
    """Handle route b which is Jump out of bed. This branch offers up to three decisions."""
    # I set the scene for the second branch
    print("You jump out of bed. What is next?")
    # I present the first set of actions using the required print helper
    print_choices("Take a quick shower", "Brush your teeth", "Get dressed")
    # I read the first decision using the validator that enforces a or b or c
    first = get_valid_choice()

    # I branch on the first decision and guide the flow to the next menu
    if first == "a":
        # The player chose a quick shower
        print("You take a quick shower.")
        print("Final step before you leave?")
        # I give three options. The third option is the direct leave choice
        print_choices("Take another shower", "Brush your teeth", "Head to school now")
        second = get_valid_choice()

        if second == "a":
            # Two showers take too long
            print("You spend too long in the bathroom.")
            print("You are late for class and get kicked out of Stevens.")
            print("Game over.")
            return
        elif second == "b":
            # Clean and minty now decide whether to go or waste time
            print("Clean and minty. Do you change or go?")
            print_choices("Change outfits", "Check your phone", "Head to school now")
            third = get_valid_choice()
            if third == "c":
                # The player leaves on time
                print("You are clean, minty, and presentable.")
                print("You arrive on time to CS 115.")
                print("You win.")
            else:
                # The player wastes time after getting ready
                print("You wasted time after getting ready.")
                print("You are late for class and get kicked out of Stevens.")
                print("Game over.")
        elif second == "c":
            # The player leaves without brushing or dressing up
            print("You are clean but skipped brushing and dressing nicely.")
            print("At least you made it to class.")

    elif first == "b":
        # The player chose brushing first
        print("You brush your teeth.")
        print("Final step before you leave?")
        print_choices("Take a quick shower", "Brush again", "Head to school now")
        second = get_valid_choice()

        if second == "a":
            # Clean and minty now decide whether to dress or go
            print("Clean and minty. Do you dress or go?")
            print_choices("Get dressed", "Admire your reflection", "Head to school now")
            third = get_valid_choice()
            if third == "a":
                # Dressing takes too long here
                print("You spend too long picking an outfit.")
                print("You are late for class and get kicked out of Stevens.")
                print("Game over.")
            elif third == "b":
                # Admiring the mirror also wastes time
                print("You linger and lose time. You are late for class.")
                print("Game over.")
            elif third == "c":
                # Leave right now even in pajamas
                print("You are clean, minty, and still in pajamas.")
                print("You make it to class anyway.")
        elif second == "b":
            # Brushing twice wastes time
            print("You brush again and lose track of time.")
            print("You are late for class and get kicked out of Stevens.")
            print("Game over.")
        elif second == "c":
            # Leave now after brushing
            print("You are minty fresh but a bit messy.")
            print("At least you made it to class.")

    elif first == "c":
        # The player chose to get dressed first
        print("You get dressed.")
        print("Final step before you leave?")
        print_choices("Take a quick shower", "Brush your teeth", "Head to school now")
        second = get_valid_choice()

        if second == "a":
            # Dressed and showered. Now allow brushing or leaving
            print("You are clean and sharp. Do you brush or go?")
            print_choices("Brush your teeth", "Change outfits again", "Head to school now")
            third = get_valid_choice()
            if third == "a":
                # All three boxes checked and on time
                print("Clean, minty, and well dressed.")
                print("You arrive on time to CS 115.")
                print("You win.")
            elif third == "b":
                # Changing again wastes time
                print("You change again and lose time.")
                print("You are late for class and get kicked out of Stevens.")
                print("Game over.")
            elif third == "c":
                # Leave without brushing
                print("You skip brushing but make it to class.")
        elif second == "b":
            # Dressed and minty. Now decide to shower or leave
            print("You are minty and well dressed.")
            print("Do you shower or go?")
            print_choices("Quick shower", "Rebrush for no reason", "Head to school now")
            third = get_valid_choice()
            if third == "a":
                # Showering now causes a delay
                print("You spend too long and arrive late.")
                print("Game over.")
            elif third == "b":
                # Rebrushing causes a delay
                print("You brush again and run late.")
                print("Game over.")
            elif third == "c":
                # Leave right away
                print("You make it to class on time.")
        elif second == "c":
            # Leave dressed without other tasks
            print("You are well dressed but smell a bit off.")
            print("At least you made it to class.")


def route_c():
    """Handle route c which is Snooze. Exactly two decisions. The second must be school or you lose."""
    # I explain the constraint so the player understands the time pressure
    print("You snooze for ten minutes. Time is tight.")
    print("First action:")
    # I show the first menu with three valid choices
    print_choices("Take a quick shower", "Brush your teeth", "Get dressed")
    first = get_valid_choice()

    # I narrate the first action so the story feels responsive
    if first == "a":
        print("You take a quick shower.")
    elif first == "b":
        print("You brush your teeth.")
    elif first == "c":
        print("You get dressed.")

    # I now present the second and final decision for this route
    print("Second action. Choose wisely. If you do not go to school now you will be late.")
    print_choices("Do another grooming task", "Wander around deciding", "Head to school now")
    second = get_valid_choice()

    # Only the school choice keeps you on time
    if second == "c":
        if first == "a":
            print("You are clean but rushed. You arrive just in time to CS 115.")
        elif first == "b":
            print("You are minty but rushed. You arrive just in time to CS 115.")
        elif first == "c":
            print("You look sharp but rushed. You arrive just in time to CS 115.")
        print("You win.")
    else:
        # I explain specific slow paths the user asked for and then end the game
        if first == "b" and second == "a":
            print("You try to brush then shower. That combo takes too long.")
        elif first == "b" and second == "b":
            print("You try to brush twice. That takes too long.")
        elif first == "a" and second == "a":
            print("Two grooming tasks in a row take too long.")
        else:
            print("You spend too long getting ready.")
        print("You are late for class and get kicked out of Stevens.")
        print("Game over.")


def my_story():
    """Run the story from the beginning using only the approved helpers and menus."""
    # I open with the setup and then present the very first choice
    print("You wake up in the morning and check your alarm clock.")
    print("You are late for school.")
    print("How do you start your morning?")
    print_choices("Sleep a little longer", "Jump out of bed", "Snooze the alarm")
    user_choice = get_valid_choice()

    # I call the proper route based on the first choice
    if user_choice == "a":
        route_a()
    elif user_choice == "b":
        route_b()
    elif user_choice == "c":
        route_c()
