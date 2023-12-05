# Runtime
# 23ms
# Beats 99.48%of users with Python3

# Memory
# 16.25MB
# Beats 35.39%of users with Python3

class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            if n % 2 == 1:
                n = int(n / 2)
                matches += n
                n += 1
            else:
                n = int(n / 2)
                matches += n

        return matches
