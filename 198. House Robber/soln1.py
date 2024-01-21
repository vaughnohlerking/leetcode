# Runtime
# 23ms
# Beats 99.66% of users with Python3

# Memory
# 16.60MB
# Beats 57.82% of users with Python3

# [ Time taken: 13 m 16 s ]

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxes = [0]*n
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        elif n== 3:
            return max(nums[0] + nums[2], nums[1])
        maxes[0] = nums[0]
        maxes[1] = nums[1]
        maxes[2] = nums[2]
        for i in range(2,n):
            maxes[i] = max(maxes[i-2], maxes[i-3]) + nums[i]
        return max(maxes)
        
