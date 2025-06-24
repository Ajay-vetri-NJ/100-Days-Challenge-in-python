def fibonacci(n):
    # Initial two numbers of the Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generating Fibonacci numbers until we have n numbers
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    # Return only the first 'n' numbers
    return fib_sequence[:n]

# Input from the user
n_terms = int(input("Enter the number of terms: "))

# Handle case where n is less than 1
if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    # Generate and display Fibonacci sequence
    result = fibonacci(n_terms)
    print(f"Fibonacci sequence with {n_terms} terms: {result}")
