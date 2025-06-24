from collections import deque

def sliding_window_max(nums, k):
    
    dq = deque()
    result = []

    for i in range(len(nums)):
        
        if dq and dq[0] == i - k:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
k = int(input("Enter the size of the sliding window: "))

max_in_windows = sliding_window_max(nums, k)
print(f"The maximum values in each sliding window of size {k} are: {max_in_windows}")