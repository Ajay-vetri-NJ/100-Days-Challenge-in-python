import random
import string

def generate_password(length=12):
    if length < 4:
        print("Password length must be at least 4.")
        return None

    letters = string.ascii_letters  
    digits = string.digits  
    symbols = string.punctuation  

    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    all_characters = letters + digits + symbols
    password += random.choices(all_characters, k=length - 3)

    random.shuffle(password)

    return ''.join(password)

try:
    length = int(input("Enter desired password length (minimum 4): "))
    password = generate_password(length)
    if password:
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid integer for password length.")