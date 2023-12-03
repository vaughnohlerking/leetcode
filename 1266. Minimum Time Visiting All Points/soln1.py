#70ms
#Beats 24.30%of users with Python3

#16.46MB
#Beats 5.31%of users with Python3

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        for i in range(1, len(points)):
            total += self.calcDist(points[i], points[i-1])
        return total

    def calcDist(self, p1: List[int], p2: List[int]) -> int:
        return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
