def count_occurrences(input_list):
    occurrences = {}
    for item in input_list:
        occurrences[item] = occurrences.get(item, 0) + 1
    return occurrences

try:
    user_input = input("Enter a list of elements separated by spaces: ")
    input_list = user_input.split() 
     
    result = count_occurrences(input_list)
    
    print("\nOccurrences of each element:")
    for key, value in result.items():
        print(f"{key}: {value}")
except Exception as e:
    print(f"An error occurred: {e}")