# Runtime
# 135ms
# Beats 17.41%of users with Python

# Memory
# 14.32MB
# Beats 19.43%of users with Python

class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        n = len(nums) - 1
        return nums[n] * nums[n-1] - nums[0] * nums[1]
