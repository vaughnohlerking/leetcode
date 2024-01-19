# Runtime
# 119ms
# Beats 82.39% of users with Python3

# Memory
# 17.33 MB
# Beats 70.38% of users with Python3

# dynamic programming solution
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        
        mins = [[0 for i in range(n)] for j in range(n)]

        # init first row
        for i in range(n):
            mins[0][i] = matrix[0][i]

        minSum = 100 * n

        # iterate through array and store minimums dynamically
        for i in range(1,n):
            for j in range(n):
                if j > 0 and j < n - 1:
                    mins[i][j] = matrix[i][j] + min(mins[i-1][j-1],mins[i-1][j],mins[i-1][j+1])
                elif j > 0:
                    mins[i][j] = matrix[i][j] + min(mins[i-1][j-1],mins[i-1][j])
                else:
                    mins[i][j] = matrix[i][j] + min(mins[i-1][j],mins[i-1][j+1])
                
                if i == n-1:
                    minSum = min(minSum, mins[i][j])

        return minSum
