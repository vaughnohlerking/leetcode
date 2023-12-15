# Runtime
# 65ms
# Beats 36.41%of users with Python3

# Memory
# 16.57MB
# Beats 13.03%of users with Python3

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        myDict = {}

        for i in range(len(paths)):
            for j in range(2):

                val = myDict.get(paths[i][j])
                
                if val == None:
                    myDict[paths[i][j]] = "start" if j == 0 else "dest"
                else:
                    myDict[paths[i][j]] = "journey"

        print(myDict)

        for dest in myDict:
            if myDict[dest] == "dest":
                return dest
