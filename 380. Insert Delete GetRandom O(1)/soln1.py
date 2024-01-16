# Runtime
# 391ms
# Beats 43.00% of users with Python3

# Memory 
# 65.02MB
# Beats 6.72% of users with Python3

class RandomizedSet:

    def __init__(self):
        self.numSet = {}

    def insert(self, val: int) -> bool:
        if val in self.numSet:
            return False
        else:
            self.numSet[val] = 0
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.numSet:
            del self.numSet[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.numSet.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
