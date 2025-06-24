def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Step 1: Create buckets
    max_value = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    
    # Step 2: Distribute array elements into buckets
    for num in arr:
        index = int(num * bucket_count / (max_value + 1))
        buckets[index].append(num)
    
    # Step 3: Sort individual buckets and concatenate
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

# User input
try:
    arr = list(map(float, input("Enter numbers separated by spaces: ").split()))
    print("Sorted array:", bucket_sort(arr))
except ValueError:
    print("Please enter valid numbers.")
