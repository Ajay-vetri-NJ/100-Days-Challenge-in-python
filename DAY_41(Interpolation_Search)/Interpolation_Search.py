def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((high - low) * (target - arr[low]) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1 

arr = list(map(int, input("Enter sorted elements (space-separated): ").split()))
target = int(input("Enter target element to search for: "))

index = interpolation_search(arr, target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")
