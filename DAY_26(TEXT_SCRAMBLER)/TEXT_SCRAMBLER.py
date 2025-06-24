import random

def scramble_word(word):
    word = list(word)  # Convert the word into a list of characters
    random.shuffle(word)  # Shuffle the characters
    return ''.join(word)  # Join the list back into a string

def word_scramble_game():
    words = ['python', 'programming', 'challenge', 'computer', 'science', 'scramble', 'game', 'keyboard']
    selected_word = random.choice(words)  # Randomly select a word
    scrambled = scramble_word(selected_word)  # Get the scrambled version

    print("Welcome to the Word Scramble Game!")
    print("Unscramble the letters to form a word:")
    print(scrambled)

    attempts = 3  # Allow the player three attempts to guess the word

    while attempts > 0:
        guess = input("Your guess: ").strip().lower()  # Get the player's guess

        if guess == selected_word:
            print("Congratulations! You guessed the word correctly.")
            break
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
            if attempts == 0:
                print(f"Sorry, you're out of attempts. The word was '{selected_word}'.")

if __name__ == "__main__":
    word_scramble_game()
