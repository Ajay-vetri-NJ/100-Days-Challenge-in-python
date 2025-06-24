class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def main():
    trie = Trie()
    
    while True:
        print("\nMenu:")
        print("1. Insert a word")
        print("2. Search for a word")
        print("3. Check if prefix exists")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            word = input("Enter the word to insert: ")
            trie.insert(word)
            print(f"Word '{word}' inserted.")
        elif choice == 2:
            word = input("Enter the word to search: ")
            found = trie.search(word)
            if found:
                print(f"Word '{word}' found in the Trie.")
            else:
                print(f"Word '{word}' not found in the Trie.")
        elif choice == 3:
            prefix = input("Enter the prefix to check: ")
            exists = trie.starts_with(prefix)
            if exists:
                print(f"Prefix '{prefix}' exists in the Trie.")
            else:
                print(f"Prefix '{prefix}' does not exist in the Trie.")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
