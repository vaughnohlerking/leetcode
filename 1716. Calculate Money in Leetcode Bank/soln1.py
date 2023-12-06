# 48ms beats 12.75
# 16.4mb beats 8%

class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = int(n/ 7)
        dayOfWeek = n % 7
        fullWeek = 28
        total = 0
        for i in range(weeks):
            total += fullWeek + 7 * i

        for i in range(dayOfWeek):
            total += i + weeks + 1

        return total
