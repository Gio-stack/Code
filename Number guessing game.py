# number guessing game with guess limit
import random

user_guess = ""
answer = random.randint(0, 100)
guess_limit = 3
number_of_guesses = 0
win = user_guess == answer
out_of_guesses = False

print("Welcome to the number guessing game, you will need too guess a number between 1 and 100 to win.")
print("You only have 3 tries to guess the correct number, make a wise choice!")

while user_guess != answer and not out_of_guesses:
    if number_of_guesses < guess_limit:
        user_guess = int(input("Enter your first guess: "))
        if user_guess >= answer:
            print("you are to high")
        if user_guess <= answer:
            print("you are to low")
        number_of_guesses += 1
    if number_of_guesses == 1 and user_guess != answer:
        user_guess = int(input("Try again: "))
        if user_guess >= answer:
            print("you are to high")
        if user_guess <= answer:
            print("you are to low")
        number_of_guesses += 1
    if number_of_guesses == 2 and user_guess != answer:
        user_guess = int(input("Last chance to win!: "))
        number_of_guesses += 1
    else:
        out_of_guesses = True


if user_guess == answer:
    print("What in the world! you won!!! the number was: " + str(answer))
if out_of_guesses:
    print("You are out of guesses!, The answer was: " + str(answer) + " pretty sweet right!")
