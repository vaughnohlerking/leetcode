# Runtime
# 1482ms
# Beats 19.65%of users with Python3

# Memory
# 50.95MB
# Beats 72.86%of users with Python3

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        M = len(grid)
        N = len(grid[0])
        maxMN = max(M,N)
        rowSum = [0] * M
        colSum = [0] * N
        diff = [ [0] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                rowSum[i] += 1 if grid[i][j] == 1 else -1
        for i in range(N):
            for j in range(M):
                colSum[i] += 1 if grid[j][i] == 1 else -1
        for i in range(M):
            for j in range(N):
                diff[i][j] += rowSum[i]
        for i in range(N):
            for j in range(M):
                diff[j][i] += colSum[i]

        return diff
