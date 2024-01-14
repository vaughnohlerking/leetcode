# Runtime
# 412ms
# Beats 5.00% of users with Python3

# Memory
# 21.68MB
# Beats 5.26% of users with Python3

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
        dict2 = dict1.copy()
        if len(word1) != len(word2):
            return False
        
        for i in range(len(word1)):
            dict1[word1[i]] = dict1.get(word1[i]) + 1
            dict2[word2[i]] = dict2.get(word2[i]) + 1

        zeroProf1 = ''
        zeroProf2 = ''

        for e in dict1:
            zeroProf1 += str(dict1[e] if dict1[e] < 10 else 9)
        for e in dict2:
            zeroProf2 += str(dict2[e] if dict2[e] < 10 else 9)

        for i in range(26):
            if zeroProf1[i] == "0" and zeroProf2[i] != "0":
                return False
            elif zeroProf2[i] == "0" and zeroProf1[i] != "0":
                return False

        profile1 = []
        profile2 = []
        
        for i in range(len(word1)):
            profile1.append(dict1[word1[i]])
            profile2.append(dict2[word2[i]])
        
        profile1.sort()
        profile2.sort()
        for i in range(len(profile1)):
            if profile1[i] != profile2[i]:
                return False

        return True
