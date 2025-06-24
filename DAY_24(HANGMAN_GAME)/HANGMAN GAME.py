import random

def hangman():
    words = ["python", "hangman", "programming", "development", "challenge"]
    chosen_word = random.choice(words)
    guessed_letters = []
    attempts = 6
    word_completion = "_" * len(chosen_word)
    
    print("Welcome to Hangman!")
    print(f"The word has {len(chosen_word)} letters: {word_completion}")
    
    while attempts > 0 and "_" in word_completion:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print(f"Good guess! '{guess}' is in the word.")
            word_completion = "".join(
                [letter if letter in guessed_letters else "_" for letter in chosen_word]
            )
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {attempts} attempts left.")

        print(f"Current word: {word_completion}")

    if "_" not in word_completion:
        print(f"Congratulations! You've guessed the word: '{chosen_word}'")
    else:
        print(f"Game over! The word was: '{chosen_word}'")
        
if __name__ == "__main__":
    hangman()
