emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😡",
    "love": "❤",
    "tired": "😴",
    "excited": "😄",
    "funny": "😂",
    "cool": "😎"
}

def emoji_translator(sentence):
    words = sentence.split()
    translated_words = [emoji_dict.get(word, word) for word in words]
    return " ".join(translated_words)

user_input = input("Enter a sentence: ")
translated_sentence = emoji_translator(user_input)

print("Translated Sentence:", translated_sentence)