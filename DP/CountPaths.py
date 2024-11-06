class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m) ] # dp[i][j] means the number of ways to reach the cell (i,j)
        
        dp[0][0] = 1

        # The cells that are on the first line are reached by just one single possible move 
        for j in range(n):
            dp[0][j] = 1
        
        #The cells at the left column

        for i in range(m):

            dp[i][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

s = Solution()
print(s.uniquePaths(3,6))
