import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 20.")

secret_number = random.randint(1, 20)
tries = 0
max_tries = 5

while tries < max_tries:
    guess = int(input("Enter your guess: "))
    tries += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed the number in {tries} tries.")
        break
else:
    print(f"Sorry! The number was {secret_number}.")

print("Game over!")
