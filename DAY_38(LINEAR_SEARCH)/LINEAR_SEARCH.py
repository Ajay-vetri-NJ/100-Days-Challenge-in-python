def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i  # Returns the index of the target
    return -1  # Target not found

# Get user input
arr = list(map(int, input("Enter elements of the list separated by spaces: ").split()))
target = int(input("Enter the target element to search for: "))

# Perform search
result = linear_search(arr, target)

# Display result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")