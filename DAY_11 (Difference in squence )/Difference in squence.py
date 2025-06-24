# Define a function named test_distinct that takes a list 'data' as a parameter.
def test_distinct(data):
    # Check if the length of the list is equal to the length of the set created from the list.
    if len(data) == len(set(data)):
        # If the lengths are equal, it means all elements in the list are distinct.
        return True
    else:
        # If the lengths are not equal, there are duplicate elements in the list.
        return False

# Call the test_distinct function with a list [1, 5, 7, 9] and print the result.
print(test_distinct([1, 5, 7, 9]))

# Call the test_distinct function with a list [2, 4, 5, 5, 7, 9] and print the result.
print(test_distinct([2, 4, 5, 5, 7, 9]))
