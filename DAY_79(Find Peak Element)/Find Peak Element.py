def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

peak_index = find_peak_element(nums)
print(f"The index of a peak element is: {peak_index}")
print(f"The peak element is: {nums[peak_index]}")
