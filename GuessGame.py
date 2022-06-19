import random
from Live import validate

difficulty = 200
secret_number = 0


# 1. generate_number - Will generate number between 1 to difficulty and save it to secret_number.
def generate_number():
    global secret_number
    secret_number = random.randint(1, difficulty)


# 2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and return the number.

def get_guess_from_user():
    prompt = f"Please choose a number between 1 to {difficulty}\n"
    number_from_user = validate(prompt, 1, difficulty)
    return number_from_user


# 3. compare_results - Will compare the the secret generated number to the one prompted by the get_guess_from_user.

def compare_results(guess_from_user):
    if secret_number == guess_from_user:
        return 0
    else:
        return 1


# 4. play - Will call the functions above and play the game. Will return True / False if the user lost or won.
def play(game_difficulty):
    global difficulty
    difficulty = game_difficulty
    generate_number()
    guess = get_guess_from_user()
    comparison = compare_results(guess)
    if comparison == 0:
        print("Good guess! u won!\n\n")
        return True
    elif comparison == 1:
        print(f"Try again! the secret number was {secret_number}\n\n")
        return False
    else:
        return "something failed"
