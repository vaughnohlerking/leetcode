# Runtime
# 679ms
# Beats 47.73%of users with Python

# Memory
# 59.56MB
# Beats 52.27%of users with Python

class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        xpoints = [0] * len(points)
        for i in range(len(points)):
            xpoints[i] = points[i][0]
        xpoints.sort()
        print(xpoints)
        widest = 0
        for i in range(1, len(points)):
            widest = max(widest, xpoints[i] - xpoints[i-1])
        return widest
