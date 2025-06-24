from collections import defaultdict, deque

def alien_order(words):
    graph = defaultdict(set)
    in_degrees = defaultdict(int)
    
    for word in words:
        for char in word:
            in_degrees[char] = 0
    
    for i in range(len(words) - 1):
        first, second = words[i], words[i + 1]
        min_length = min(len(first), len(second))
        for j in range(min_length):
            if first[j] != second[j]:
                if second[j] not in graph[first[j]]:
                    graph[first[j]].add(second[j])
                    in_degrees[second[j]] += 1
                break
        else:
            if len(second) < len(first):
                return ""
    
    queue = deque([char for char in in_degrees if in_degrees[char] == 0])
    order = []
    
    while queue:
        current = queue.popleft()
        order.append(current)
        
        for neighbor in graph[current]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)
    
    if len(order) == len(in_degrees):
        return "".join(order)
    else:
        return ""

words = input("Enter the sorted list of words (comma-separated): ").split(',')
words = [word.strip() for word in words]

alien_language_order = alien_order(words)
print(f"The order of letters in the alien language is: {alien_language_order}")
