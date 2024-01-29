# Runtime
# 28ms
# Beats 94.37% of users with Python3

# Memory
# 16.63MB
# Beats 59.92% of users with Python3

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        if len(self.s1) == 0:
            self.s2.append(x)
        else:
            self.s1.append(x)
            
        # print("1:", self.s1, "2:",self.s2)

    def pop(self) -> int:
        val = 0
        if len(self.s1) == 0:
            for i in range(len(self.s2)):
                self.s1.append(self.s2.pop())
            # print("boutta pop 1.    1:", self.s1, "     2:",self.s2)
            val = self.s1.pop()
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        else:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
            # print("boutta pop 2.    1:", self.s1, "     2:",self.s2)
            val = self.s2.pop()
            for i in range(len(self.s2)):
                self.s1.append(self.s2.pop())
        return val
        

    def peek(self) -> int:
        val = 0
        if len(self.s1) == 0:
            for i in range(len(self.s2)):
                self.s1.append(self.s2.pop())
            # print("boutta peek 1.    1:", self.s1, "     2:",self.s2)
            val = self.s1[-1]
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        else:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
            # print("boutta peek 2.    1:", self.s1, "     2:",self.s2)
            val = self.s2[-1]
            for i in range(len(self.s2)):
                self.s1.append(self.s2.pop())
        return val
        

    def empty(self) -> bool:
        return True if len(self.s1) == 0 and len(self.s2) == 0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
