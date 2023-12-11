# Runtime
# 106ms
# Beats 29.01%of users with Python3

# Memory
# 17.63MB
# Beats 59.65%of users with Python3

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
    
        length = len(arr)
        if length == 1:
            return arr[0]
        quarter = int(length / 4)
        for i in range(length - 1):
            if arr[i] == arr[i + 1]:
                if arr[i] == arr[i + quarter]:
                    return arr[i]
            
