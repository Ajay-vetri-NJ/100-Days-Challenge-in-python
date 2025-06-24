import re

def check_password_strength(password):
    
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search("[a-z]", password) is not None
    uppercase_criteria = re.search("[A-Z]", password) is not None
    digit_criteria = re.search("[0-9]", password) is not None
    special_char_criteria = re.search("[@#$%^&+=]", password) is not None

    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    if criteria_met == 5:
        return "Strong"
    elif criteria_met >= 3:
        return "Medium"
    else:
        return "Weak"

password = input("Enter a password to check its strength: ")

strength = check_password_strength(password)
print(f"Password Strength: {strength}")