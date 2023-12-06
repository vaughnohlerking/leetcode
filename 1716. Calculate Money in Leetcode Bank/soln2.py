# came up with this solution with a litttle bit of help from leetcode and research into sums of arithmetic series. Simple math, I'd just forgotten it existed for my first solution

# Runtime
# 41ms
# Beats 48.52%of users with Python3

# Memory
# 16.27MB
# Beats 40.52%of users with Python3

class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        dayOfWeek = n % 7

        total = ((weeks * (weeks - 1)) // 2) * 7
        total += weeks * 28
        total += ((dayOfWeek * (dayOfWeek + 1)) // 2 + (weeks * dayOfWeek))

        return total
