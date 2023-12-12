# Runtime
# 58ms
# Beats 48.52%of users with Python3

# Memory
# 16.35MB
# Beats 41.49%of users with Python3

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxes = [nums[0], 0]
        if len(nums) == 2:
            return (nums[0] - 1) * (nums[1] - 1)
        for i in range(len(nums)):
            if nums[i] >= maxes[0]:
                maxes[0] = nums[i]
                maxes.sort()
        print(maxes)
        return (maxes[0] - 1) * (maxes[1] - 1)
        
