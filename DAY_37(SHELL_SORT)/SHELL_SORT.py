def shell_sort(arr):
    n = len(arr)
    gap = n//2  

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  

    return arr

user_input = input("Enter numbers separated by spaces: ")
arr = list(map(int, user_input.split()))  

sorted_arr = shell_sort(arr)
print("Sorted array:", sorted_arr)