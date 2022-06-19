# This game will use the free currency api to get the current exchange rate from USD to ILS, will
# generate a new random number between 1-100 a will ask the user what he thinks is the value of
# the generated number from USD to ILS, depending on the user’s difficulty his answer will be
# correct if the guessed value is between the interval surrounding the correct answer
#
# Properties
# 1. Difficulty
import requests
import random
from Live import check_user_input

difficulty = 3


# Methods
# 1. get_money_interval -Will get the current currency rate from USD to ILS and will
# generate an interval as follows:
# a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
# (5 - d))

def get_money_interval(amount):
    global difficulty
    current_currency = get_currency()
    total_value = current_currency * amount
    interval = [(total_value - (5 - difficulty)), total_value + (5 - difficulty)]
    return interval


def get_currency():
    url = F"https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount=1"
    payload = {}
    headers = {
        "apikey": "oSyNwU9mVXpXQIfYvm3UQwiu3wjn4FyJ"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()["result"]


# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
# value to a given amount of USD
def get_guess_from_user(amount):
    prompt = f"please enter what do u think is the value of {amount} from USD to ILS\n"
    input_from_user = input(prompt)
    val = check_user_input(input_from_user)
    return val


# 3. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.
def play(global_difficulty):
    global difficulty
    difficulty = global_difficulty
    amount = random.randint(1, 100)
    val = get_guess_from_user(amount)
    interval = get_money_interval(amount)
    if interval[0] <= val <= interval[1]:
        print("Good guess! u won!\n\n")
        return True
    else:
        real_value = amount * get_currency()
        print(f"Try again! the real value is {real_value}\n\n")
        return False
