def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1  
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

try:
    user_input = input("Enter numbers separated by spaces: ")
    arr = [int(num) for num in user_input.split()]

    radix_sort(arr)
    print("Sorted array:", arr)

except ValueError:
    print("Please enter valid integers.")