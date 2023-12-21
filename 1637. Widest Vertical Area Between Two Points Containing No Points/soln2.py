# submitting a second solution because i realized python will sort a 2d array by first index just like i need. Not sure why it got a slower time, maybe leetcode's servers were bogged down 27 minutes after releasing the new daily problem

# Runtime
# 940ms
# Beats 6.82%of users with Python

# Memory
# 59.41MB
# Beats 81.82%of users with Python

class Solution(object):
    def maxWidthOfVerticalArea(self, points):

        points.sort()
        print(points)
        widest = 0
        for i in range(1, len(points)):
            widest = max(widest, points[i][0] - points[i-1][0])
        return widest
