# Runtime
# 41ms
# Beats 67.89%of users with Python3

# Memory
# 16.39MB
# Beats 24.76%of users with Python3

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxDig = "-1"
        for i in range(2, len(num)):
            if num[i] == num[i - 1] and num[i - 1] == num[i - 2]:
                maxDig = max(maxDig, num[i])
        return maxDig + maxDig + maxDig if maxDig != "-1" else ""
