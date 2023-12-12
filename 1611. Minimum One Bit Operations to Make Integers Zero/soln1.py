# Runtime
# 44ms
# Beats 28.24%of users with Python3

# Memory
# 16.35MB
# Beats 32.12%of users with Python3

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:

        bin = self.decToBin(n)
        length = len(bin)
        multiplier = 1
        total = 0
        for i in range(length):
            if bin[i] == "1":
                exp = length - i
                total += multiplier * ((2**exp) - 1)
                multiplier *= -1
        return total

    def decToBin(self, n: int) -> str:
        bin = ""
        if n == 0:
            return "0"
        while n >= 1:
            bin = str(int(n % 2)) + bin
            n = n / 2
        return bin
