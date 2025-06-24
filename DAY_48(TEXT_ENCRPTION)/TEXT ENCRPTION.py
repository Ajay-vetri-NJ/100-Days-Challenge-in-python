def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char

    return encrypted_text

def main():
    print("Welcome to the Caesar Cipher Encryption Program!")
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted_text = encrypt(text, shift)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
