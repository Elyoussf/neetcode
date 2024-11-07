from typing import *

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # Initialize dp array with (m+1)x(n+1) size
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[j - 1] == text2[i - 1]:  # Match found
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]  # The answer is in the bottom-right corner of dp matrix


