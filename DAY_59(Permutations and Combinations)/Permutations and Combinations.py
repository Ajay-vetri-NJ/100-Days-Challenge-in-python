from itertools import permutations, combinations

def generate_permutations(elements):
    perm = permutations(elements)
    print("\nPermutations:")
    for p in perm:
        print(p)

def generate_combinations(elements, r):
    comb = combinations(elements, r)
    print("\nCombinations:")
    for c in comb:
        print(c)

def main():
    print("Welcome to the Permutations and Combinations Generator!")
    
    elements = input("Enter the elements separated by space: ").split()
    while True:
        print("\nMenu:")
        print("1. Generate Permutations")
        print("2. Generate Combinations")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            generate_permutations(elements)
        elif choice == 2:
            r = int(input("Enter the number of elements in each combination: "))
            generate_combinations(elements, r)
        elif choice == 3:
            print("Thank you for using the generator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()