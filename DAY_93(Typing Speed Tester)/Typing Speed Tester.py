import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python programming is both fun and powerful.",
    "A journey of a thousand miles begins with a single step.",
    "Practice makes perfect, so keep typing.",
    "Artificial Intelligence is shaping the future."
]

def typing_speed_tester():
    print("Welcome to the Typing Speed Tester!")
    print("Type the sentence shown below as quickly and accurately as you can.\n")
    
    sentence = random.choice(sentences)
    print(f"Your sentence is:\n\"{sentence}\"")
    input("\nPress Enter when you're ready to start...")
    
    start_time = time.time()
    
    user_input = input("\nStart typing: ")
    
    end_time = time.time()
    
    time_taken = end_time - start_time  
    words_typed = len(user_input.split())
    wpm = (words_typed / time_taken) * 60  
    
    correct_chars = sum(1 for a, b in zip(sentence, user_input) if a == b)
    accuracy = (correct_chars / len(sentence)) * 100 if sentence else 0
    
    print("\n--- Typing Test Results ---")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Words Per Minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")
    
    if accuracy == 100:
        print("Excellent! You typed perfectly!")
    elif accuracy > 80:
        print("Great job! A little more practice and you'll be perfect.")
    else:
        print("Keep practicing to improve your speed and accuracy!")

typing_speed_tester()