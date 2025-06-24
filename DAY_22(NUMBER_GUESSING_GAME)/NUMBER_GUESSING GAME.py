import random

random_number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess == random_number:
        print(f"Congratulations! You guessed the number {random_number}.")
        break
    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
