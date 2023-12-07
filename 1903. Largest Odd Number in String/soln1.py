# Runtime
# 46ms
# Beats 90.49%of users with Python3

# Memory
# 18.01MB
# Beats 6.48%of users with Python3

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        else:
          return ""
