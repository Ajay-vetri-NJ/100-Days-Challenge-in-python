def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

number_of_paths = unique_paths(m, n)
print(f"The number of unique paths from the top-left corner to the bottom-right corner is: {number_of_paths}")
