def simple_hash(text):
    hash_value = 0
    for char in text:
        hash_value = (hash_value * 31 + ord(char)) % (2**32)
    return hash_value

def get_user_input():
    while True:
        text = input("Enter the text to hash: ")
        if text:
            return text
        else:
            print("Input cannot be empty. Please enter some text.")

def display_result(original, hashed):
    print("\n--- Hashing Result ---")
    print(f"Original Text: {original}")
    print(f"Simple Hash: {hashed}")
    print("----------------------\n")

def main():
    print("Welcome to the Simple Hashing Program!")
    text = get_user_input()
    hashed_text = simple_hash(text)
    display_result(text, hashed_text)

if __name__ == "__main__":
    main()