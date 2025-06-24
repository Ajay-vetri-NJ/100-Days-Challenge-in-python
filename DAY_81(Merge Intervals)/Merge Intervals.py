def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
        
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

intervals_input = input("Enter the intervals (e.g., [1,3],[2,6],[8,10],[15,18]): ")
intervals = [list(map(int, interval.split(','))) for interval in intervals_input.strip('[]').split('],[')]

merged_intervals = merge_intervals(intervals)
print(f"The merged intervals are: {merged_intervals}")
