# Runtime
# 47 ms
# Beats 38.67% of users with Python3

# Memory
# 17.56 MB
# Beats 9.52% of users with Python3

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(arr) == 1:
            return True
        nums = {}
        for num in arr:
            if num in nums:
                nums[num] = nums.get(num) + 1
            else:
                nums[num] = 1
        count = []
        for num in nums:
            count.append(nums[num])
        count.sort()
        for i in range(1, len(count)):
            if count[i] == count[i-1]:
                return False
        return True
        
