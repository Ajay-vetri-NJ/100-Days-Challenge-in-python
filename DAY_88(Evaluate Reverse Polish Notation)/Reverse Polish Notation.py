def eval_rpn(tokens):
    stack = []
    operators = set(["+", "-", "*", "/"])
    
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))  
    
    return stack[0]

tokens = input("Enter the RPN expression separated by spaces: ").split()

result = eval_rpn(tokens)
print(f"The result of the RPN expression is: {result}")
