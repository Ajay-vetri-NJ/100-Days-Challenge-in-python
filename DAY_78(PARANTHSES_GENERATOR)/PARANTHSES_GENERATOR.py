def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack('', 0, 0)
    return result

num_pairs = int(input("Enter the number of pairs of parentheses: "))
combinations = generate_parentheses(num_pairs)

print("All combinations of well-formed parentheses are:")
for combination in combinations:
    print(combination)