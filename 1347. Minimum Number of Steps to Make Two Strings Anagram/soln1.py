# Runtime 186ms
# Beats 44.37%
# of users with Python3

# Memory 17.96MB
# Beats 11.97%
# of users with Python3

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        tCount = sCount.copy()

        for i in range(len(s)):
            sCount[s[i]] = sCount.get(s[i]) + 1
            tCount[t[i]] = tCount.get(t[i]) + 1
        
        total = 0
        for key in sCount:
            total += abs(sCount.get(key) - tCount.get(key))/2

        return int(total)
