# Runtime
# 64ms
# Beats 55.91%of users with Python3

# Memory
# 16.38MB
# Beats 30.68%of users with Python3

class Solution:
    def minTimeToVisitAllPoints(self, p: List[List[int]]) -> int:
        t = 0
        for i in range(1, len(p)):
            t += max(abs(p[i][0] - p[i-1][0]), abs(p[i][1] - p[i-1][1]))
        return t
