# Runtime
# 444ms
# Beats 91.95% of users with Python3

# Memory
# 41.80MB
# Beats 71.35% of users with Python3

# Medium

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        dp = [[0] * n for i in range(m)]

        dp[0][0] = 1 if text1[0] == text2[0] else 0

        for i in range(1,n):
            dp[0][i] = 1 if text1[i] == text2[0] or dp[0][i-1] == 1 else 0
        for i in range(1,m):
            dp[i][0] = 1 if text1[0] == text2[i] or dp[i-1][0] == 1 else 0
            
        # print(dp)

        for i in range(1,n):
            for j in range(1,m):
                # print(j, i)
                if text1[i] == text2[j]:
                    dp[j][i] = dp[j-1][i-1] + 1
                    # print("letter match:", text1[i])
                else:
                    dp[j][i] = max(dp[j-1][i], dp[j][i-1])#, dp[j-1][i-1])
        # print(dp)

        return dp[m-1][n-1]
