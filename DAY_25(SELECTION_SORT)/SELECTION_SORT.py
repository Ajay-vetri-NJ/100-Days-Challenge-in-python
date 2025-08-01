def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

user_input = input("Enter numbers separated by spaces: ")
arr = list(map(int, user_input.split()))

print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)