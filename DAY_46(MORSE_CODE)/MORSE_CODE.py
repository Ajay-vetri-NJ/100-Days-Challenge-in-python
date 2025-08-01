morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

morse_to_text_dict = {value: key for key, value in morse_code_dict.items()}

def text_to_morse(text):
    return ' '.join(morse_code_dict[char] for char in text.upper() if char in morse_code_dict)

def morse_to_text(morse_code):
    return ''.join(morse_to_text_dict[code] for code in morse_code.split() if code in morse_to_text_dict)

choice = input("Enter 1 to convert text to Morse code, or 2 to convert Morse code to text: ")

if choice == '1':
    text = input("Enter the text to convert to Morse code: ")
    print("Morse Code:", text_to_morse(text))
elif choice == '2':
    morse_code = input("Enter the Morse code to convert to text (use spaces between letters and '/' for spaces): ")
    print("Text:", morse_to_text(morse_code))
else:
    print("Invalid choice.")