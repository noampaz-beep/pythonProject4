# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember. If he was right
# with all the numbers the user will win otherwise he will lose.
# Properties
# 1. Difficulty
from time import sleep

from Live import check_user_input
import random

list_of_random = []
difficulty = 3


# Methods
# 1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list length will be difficulty.
def generate_sequence():
    global list_of_random
    for i in range(0, difficulty):
        list_of_random.append(random.randint(1, 101))


# 2. get_list_from_user - Will return a list of numbers prompted from the user. The list length will be in the size
# of difficulty.
def get_list_from_user():
    list_from_user = []
    for i in range(0, difficulty):
        prompt = f"Please choose a number between 1 to 101\n"
        input_from_user = input(prompt)
        new_num = check_user_input(input_from_user)
        while new_num == 0:
            input_from_user = input(prompt)
            new_num = check_user_input(input_from_user)
        list_from_user.append(new_num)
    return list_from_user


# 3. is_list_equal - A function to compare two lists if they are equal. The function will return True / False.
def is_list_equal(list_from_user):
    for i in range(0, len(list_from_user)):
        if list_from_user[i] != list_of_random[i]:
            return False
    return True


# 4. play - Will call the functions above and play the game. Will return True / False if the user lost or won.
def play(game_difficulty):
    global difficulty
    difficulty = game_difficulty
    generate_sequence()
    sleep(1)
    print("time to play!")
    user_list = get_list_from_user()
    if is_list_equal(user_list):
        print("Good guess! u won!\n\n")
        return True
    else:
        print(f"Try again! the numbers were {list_of_random}\n\n")
        return False
