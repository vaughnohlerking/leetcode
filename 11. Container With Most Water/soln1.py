# First attempt was using a basic nested loop approach to see if it would be a valid solution but it was too slow. Did a small amount of research and discovered the two pointer method and implemented it

# Runtime
# 646ms
# Beats 5.93%of users with Python3

# Memory
# 29.40MB
# Beats 5.25%of users with Python3

class Solution:
    def maxArea(self, height: List[int]) -> int:
        totalLen = len(height)
        maxx = 0
        left = 0
        right = totalLen - 1
        while left <= right:
            maxx = max(self.getArea(height,left, right),maxx)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxx

    def getArea(self, arr: List[int], i1: int, i2: int) -> int:
        height = min(arr[i1], arr[i2])
        width = i2 - i1
        return height * width
