# Runtime
# 53ms
# Beats 62.67%of users with Python3

# Memory
# 16.87MB
# Beats 49.09%of users with Python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}

        for letter in s:
            if letter in myDict:
                myDict[letter] = myDict[letter] + 1
            else:
                myDict[letter] = 1

        for letter in t:
            if letter in myDict:
                val = myDict[letter]
                if val > 1:
                    myDict[letter] = myDict[letter] - 1
                elif val == 1:
                    del myDict[letter]
            else:
                return False

        if len(myDict) == 0:
            return True

        return False
