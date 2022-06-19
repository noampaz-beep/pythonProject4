# A general purpose python file. This file will contain general information and operations we need
# for our game.
# 1. SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
# 2. BAD_RETURN_CODE - A number representing a bad return code for a function.
# 3. Screen_cleaner - A function to clear the screen (useful when playing memory game or
# before a new game starts).

import os
from time import sleep

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0


def screen_cleaner():
    os.system("cls")


# Printing Some Text
print("Hello, Welcome to Scaler!!")
print("Screen will now be cleared in 4 Seconds")

# Waiting for 4 seconds to clear the screen
sleep(4)

screen_cleaner()
