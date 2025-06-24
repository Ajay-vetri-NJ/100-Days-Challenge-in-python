def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

user_input = input("Enter numbers separated by spaces: ")
array = list(map(int, user_input.split()))

sorted_array = bubble_sort(array)
print("Sorted array:", sorted_array)
