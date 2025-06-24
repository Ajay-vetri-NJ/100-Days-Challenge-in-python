def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

nums = list(map(int, input("Enter the elements of the array separated by spaces (only 0s, 1s, and 2s): ").split()))

sort_colors(nums)
print(f"The sorted array is: {nums}")
