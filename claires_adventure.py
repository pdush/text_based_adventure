# A very short text-based adventure game written by Claire Falzone.
# Written to demonstrate what a more cleanly-written adventure game
# might look like, as an example for when designing another one.

import sys


# When reading this code, notice that each decision point is in a
# separate function, making the code simpler and not as wide. Also
# notice that there are no variable declarations all the way on the
# left (that is, outside of functions). Variables that aren't indented
# at all are called "global variables" in Python because they can be
# modified by anything else anywhere in the code, which has a tendency
# to make code harder to read. Global variables should generally be
# avoided in most programming languages.


# We don't want the user's input to be case-sensitive or have whitespace
# characters in it, so we use this function to get input.
def clean_input(prompt):
    return input(prompt).lower().strip()


def start():
    name = input("Input your name: ")

    # Notice that the string is prefixed with an 'f'. This allows us to use
    # the curly braces for putting variables in strings.
    correct_name = clean_input(f"Is {name} the name you want to use? (y/n) ")

    # If the user's input isn't what they wanted, start over
    if correct_name != 'y':
        if correct_name != 'n':
            print("Invalid input")
        start()

    forest_wakeup(name)


def forest_wakeup(name):
    print("\nYou wake up in a beautiful forest glade. All you remember is your")
    print(f"name, which is {name}.\nDo you want to get up and explore?")

    decision = clean_input("(y/n) ")
    if decision == 'y':
        explore(name)
    elif decision == 'n':
        keep_laying_down(name)
    else:
        print("Invalid input - you didn't input 'y' or 'n'.")
        forest_wakeup(name)


def explore(name):
    print("\nYou wander in the forest for a while. It's a beautiful day outside.")
    print("Birds are singing; flowers are blooming.")
    print(f"To your surprise you find \"{name}\" carved into a tree.")
    print("You don't remember doing this.")
    print("\n(The game ends here because I haven't programmed anything to happen")
    print("after this point.)")
    sys.exit(0) # the number 0 indicates to the OS that nothing bad has happened


def keep_laying_down(name):
    print("\nYou continue lying down. The wind whistles through the trees. It almost")
    print("sounds like it's calling you a fatass for sleeping so much.")
    print("\n(The game ends here because I haven't programmed anything to happen")
    print("after this point.)")
    sys.exit(0)


# Don't forget to actually call the function where your program starts.
start()
