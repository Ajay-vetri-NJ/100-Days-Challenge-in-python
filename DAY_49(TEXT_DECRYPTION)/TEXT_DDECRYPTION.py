def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text
def get_user_input():
    print("Welcome to the Caesar Cipher Decryption Program!")
    text = input("Enter the text to decrypt: ")
    shift = int(input("Enter the shift value (a positive integer): "))

    while shift < 0:
        print("The shift value should be a positive integer. Please try again.")
        shift = int(input("Enter the shift value (a positive integer): "))
    return text, shift
def main():
    text, shift = get_user_input()
    decrypted_text = decrypt(text, shift)
    print("\nOriginal Text: ", text)
    print("Shift Value: ", shift)
    print("Decrypted Text:", decrypted_text)
if __name__ == "__main__":
    main()