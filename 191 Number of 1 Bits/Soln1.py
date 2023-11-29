class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        
        while n > 0:
            bffM1 = self.biggestFittingFactor(n) - 1
            total += 1
            n -= 2 ** bffM1
        
        return total
        
    def biggestFittingFactor(self, n: int) -> int:
        i = 0
        while 2 ** i <= n:
            i += 1
        return i
