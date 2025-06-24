import random
choices = ["rock", "paper", "scissors"]
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"
while True:
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()

    if player_choice == "quit":
        print("Thanks for playing!")
        break
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    computer_choice = random.choice(choices) 
    print(f"\nYou chose {player_choice}, and the computer chose {computer_choice}.")

    result = determine_winner(player_choice, computer_choice)
    print(result + "\n")