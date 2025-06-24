def maximal_rectangle(matrix):
    if not matrix:
        return 0
    
    max_area = 0
    n = len(matrix[0])
    heights = [0] * n
    
    for row in matrix:
        for i in range(n):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        max_area = max(max_area, largest_rectangle_area(heights))
    
    return max_area

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    heights.pop()
    return max_area

print("Enter the 2D binary matrix row by row, with each row's elements separated by spaces:")
matrix = []
while True:
    row = input()
    if not row.strip():
        break
    matrix.append(row.split())

max_area = maximal_rectangle(matrix)
print(f"The maximal rectangle area is: {max_area}")
