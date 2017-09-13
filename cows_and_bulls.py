"""
Cows and Bulls
==============

The aim of the game is to guess the secret!
The secret is a 4-digit random number with no
repeated digits.
The digits are selected from 1 to 8 inclusive.
If you guess a digit correctly, whether it's in
the right place or not, you have found a cow.
If it's in the right place too, then it's a bull.
Once you've found all four bulls you will have
guessed the secret! Good luck!

"""


import random

from collections import Counter


def generate_secret():
    """
    A helper function to generate a random 4-digit number
    with no repeated digits.
    We encode it as a string because the user input will
    also be a string, and since we're only concerned with
    equality, and not numeric operations, we should make
    life easier for ourselves!
    """
    # Initialise an empty secret string
    secret = ""
    while True:
        # Select a new digit between 1 and 8 and turn it
        # into a string
        digit = str(random.randint(1, 8))
        # If the digit is not currently in the secret
        # we're safe to add it, otherwise we would have
        # repeated digits
        if digit not in secret:
            secret += digit
        # As soon as we've accumulated 4 unrepeated digits
        # we can stop adding more
        if len(secret) == 4:
            break
    # If we've broken out of the loop the secret must have
    # been populated with 4 unique digits, so return it
    return secret


def get_cows_and_bulls(guess, secret):
    """
    A helper function to generalize the process of
    comparing two inputs, a guess and a secret, and
    calculating how many cows and bulls are in the
    guess.
    Note that this function is compatible with any
    indexable object of any length. In our case the
    guess and secret are strings of length 4 composed
    entirely of digits, but this doesn't have to be
    the case. The only constraint is that they should
    not contain duplicate entries.
    """
    # Initialise new counters for cows and bulls
    # and loop over each digit of the guess and
    # where it occurs
    bulls = 0
    cows = 0
    for i, digit in enumerate(guess):
        # If the digit matches the digit in the same position
        # of the secret then we have a bull
        if digit == secret[i]:
            bulls += 1
        # Otherwise, since we know there are no duplicate digits,
        # we can just check to see if the digit is present in the
        # secret at all. If it is then we have a cow
        elif digit in secret:
            cows += 1
    return cows, bulls


def play_game():
    """
    The main function of the game
    """
    # Print the rules of the game from this module's docstring
    print(__doc__)
    # Start the game with a new secret
    secret = generate_secret()
    while True:
        guess = input('Enter a four digit guess, or "exit": ')
        # If the user wants to exit then let them know what
        # they missed
        if guess == "exit":
            print("The secret was {}\nExiting...".format(secret))
            return

        # We could split this into two checks if we want to
        # tell the user more information about why their input
        # was invalid
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input, try again")
            continue

        # Use a counter to count each digit. If the most common
        # digit occurs more than once then the user input has
        # duplicates and should be discarded
        _, most_common_digit = Counter(guess).most_common()[0]
        if most_common_digit > 1:
            print("Repeated digits! Try again")
            continue

        # Find out how many cows and bulls are in the player's guess
        cows, bulls = get_cows_and_bulls(guess, secret)

        # Let the player know how many bulls and cows they found
        print("{} bulls and {} cows".format(bulls, cows))

        # If they found all four bulls then they've guessed the secret
        # We can tell them they've won and start all over again with
        # a new secret
        if bulls == 4:
            print("You did it! Generating a new secret...")
            print("-----------------------------------------")
            secret = generate_secret()


if __name__ == "__main__":
    play_game()
