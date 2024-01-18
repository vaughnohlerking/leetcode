# Runtime
# 36ms
# Beats 65.15% of users with Python3

# Memory
# 17.17MB
# Beats 45.94% of users with Python3

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
    
        oldTotal = 0
        total = 1
        
        for i in range(2, n):
            temp = total
            total = total + oldTotal
            oldTotal = temp

        return total * 2 + oldTotal 
