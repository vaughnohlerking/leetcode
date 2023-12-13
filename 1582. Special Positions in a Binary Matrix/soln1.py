# Runtime
# 161ms
# Beats 37.92%of users with Python3

# Memory
# 16.80MB
# Beats 33.33%of users with Python3

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        height = len(mat)
        width = len(mat[0])
        rowIndex = [-1] * height
        colIndex = [-1] * width
        total = 0

        for i in range(height):
            for j in range(width):
                if mat[i][j] == 1:
                    rowIndex[i] = j if rowIndex[i] == -1 else -2
                
                
        for i in range(width):
            for j in range(height):
                if mat[j][i] == 1:
                    colIndex[i] = j if colIndex[i] == -1 else -2

        for i in range(height):
            if rowIndex[i] > -1 and colIndex[rowIndex[i]] > -1:
                total += 1
        

        return total
