class Solution:
    def knightDialer(self, n: int) -> int:
        total = 0
        if n == 0:
            return 0
        else:
            for i in range(10):
                if i == 5:
                    pass
                total += self.recurse(n - 1,i)
        return total
                

    def recurse(self, depth: int, num: int) -> int:
        total = 0
        if depth == 0:
            return 1
        else:
            nums = self.route(num)
            for number in nums:
                total += self.recurse(depth - 1, number)
            return total

    def route(self, num: int):
        if num == 1:
            return [6,8]
        elif num == 2:
            return [7,9]
        elif num == 3:
            return [4,8]
        elif num == 4:
            return [3,9,0]
        elif num == 5:
            return []
        elif num == 6:
            return [1,7,0]
        elif num == 7:
            return [2,6]
        elif num == 8:
            return [1,3]
        elif num == 9:
            return [4,2]
        else:
            return [4,6]
