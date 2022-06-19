from Live import load_game, welcome, validate

print(welcome("Guy"))
prompt = "would u like to play again? please answer 1-Yes, 2 -No\n"
input_from_user = 1
while input_from_user != 2:
    load_game()
    input_from_user = validate(prompt, 1, 2)
print("Thank you! see u next time!")
