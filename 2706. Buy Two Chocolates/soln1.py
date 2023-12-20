# Runtime
# 36ms
# Beats 73.96%of users with Python

# Memory
# 13.12MB
# Beats 87.57%of users with Python

class Solution(object):
    def buyChoco(self, prices, money):

        prices.sort()
        difference = money - (prices[0] + prices[1])
        return difference if difference >= 0 else money
