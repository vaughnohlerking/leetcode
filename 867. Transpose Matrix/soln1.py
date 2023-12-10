# Runtime
# 70ms
# Beats 78.34%of users with Python3

# Memory
# 17.11MB
# Beats 53.63%of users with Python3

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        arr = [[0] * len(matrix) for i in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                arr[j][i] = matrix[i][j]
        return arr
