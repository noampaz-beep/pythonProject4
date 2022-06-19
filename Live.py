from Score import add_score


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    prompt = "Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you " \
             "have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. " \
             "Currency Roulette - try and guess the value of a random amount of USD in ILS\n "
    print(prompt)
    choose = "Please choose game number (1-3)\n"
    game_to_play = validate(choose, 1, 3)

    choose = "Please choose game difficulty from 1 to 5:\n"
    game_difficulty = validate(choose, 1, 5)
    game_results = False
    if game_to_play == 1:
        print("Thank you!\nyou chose to play: Memory Game - a sequence of numbers will appear for 1 second and you "
              "have to guess it back")
        import MemoryGame
        game_results = MemoryGame.play(game_difficulty)
    elif game_to_play == 2:
        print('Thank you!\nyou chose to play: Guess Game - guess a number and see if you chose like the computer')
        import GuessGame
        game_results = GuessGame.play(game_difficulty)
    elif game_to_play == 3:
        print("Thank you!\nyou chose to play: Currency Roulette - try and guess the value of a random amount of USD "
              "in ILS")
        import CurrencyRouletteGame
        game_results = CurrencyRouletteGame.play(game_difficulty)
    if game_results:
        add_score(game_difficulty)
#    print(f"your game difficulty will be {game_difficulty}")


def validate(prompt, low, high):
    input_from_user = input(prompt)
    val = check_user_input(input_from_user)
    while val < low or val > high:
        input_from_user = input(prompt)
        val = check_user_input(input_from_user)
    else:
        return val


def check_user_input(input_user):
    try:
        # Convert it into integer
        val = int(input_user)
        return val
    except ValueError:
        return 0
