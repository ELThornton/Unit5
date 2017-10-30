# Elena Thornton
# 10/30/17
# guessing_a_number.py
# This program is a guessing game for the user.

import random


def begin_a_game():
    """
    This function begins the game with the user.
    It asks them if they want to play or not.
    This is also the place that the function guess_a_number() gets called from.
    :return: nothing
    """

    while True:
        begin_game = input("would you like to play a guessing game.(yes or no):", )
        if begin_game in ["yes", "no"]:
            break
    if begin_game == "yes":
        guess_a_number()
    elif begin_game == "no":
        print("goodbye")


def guess_a_number():
    """
    this is where the user guesses a number.
    this also where play_again() is called.
    :return: returns nothing.
    """
    tries = 1
    number = random.randint(1, 100)
    users_guess = input("please guess a number between 1 and 100:",)
    x = int(users_guess)
    while x != number:
        if x > number:
            print("please guess lower")
        elif x < number:
            print("please guess higher")
        tries += 1
        users_guess = input("please guess a number between 1 and 100:", )
        x = int(users_guess)

    print("It took you", tries, "tries to guess")
    play_agian()


def play_agian():
    """
    this is where the user is asked whether or not they want to play again.
    this function will call guess_a_number() if the user wants to play again.
    :return: nothing
    """
    while True:
        ask_to_play_again = input("would you like to play again (yes or no):",)
        if ask_to_play_again in ["yes", "no"]:
            break
    if ask_to_play_again == "yes":
        guess_a_number()
    elif ask_to_play_again == "no":
        print("Thanks for playing. Good Bye")


def main():
    begin_a_game()


main()
