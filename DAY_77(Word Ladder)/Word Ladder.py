from collections import deque

def word_ladder(start, end, word_list):
    word_set = set(word_list)
    if end not in word_set:
        return 0
    
    queue = deque([(start, 1)])
    
    while queue:
        current_word, current_length = queue.popleft()
        
        if current_word == end:
            return current_length
        
        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + char + current_word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, current_length + 1))
    
    return 0

start_word = input("Enter the start word: ")
end_word = input("Enter the end word: ")
word_list = input("Enter the word list (comma-separated): ").split(',')

word_list = [word.strip() for word in word_list]

result = word_ladder(start_word, end_word, word_list)
print(f"The shortest transformation sequence length is: {result}")