# Runtime
# 145ms
# Beats 97.59% of users with Python3

# Memory
# 17.77MB
# Beats 94.40% of users with Python3

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dup = 0
        missed = n

        for i in range(1,n):
            if nums[i] == nums[i-1]:
                dup = nums.pop(i)
                break

        for i in range(n-1):
            if nums[i] != i + 1:
                return[dup, i+ 1]
        return [dup, missed]
