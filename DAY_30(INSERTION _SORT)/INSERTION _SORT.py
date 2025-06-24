def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def get_user_input():
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)
    
    return arr

if __name__ == "__main__":
    arr = get_user_input()
    
    print("Original array:", arr)
    
    insertion_sort(arr)
    
    print("Sorted array:", arr)