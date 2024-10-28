class Solution:
    def climbStairs(self, n: int) -> int:
        if (n==1 or n==2):
            return n 

        dp = [0 for i in range(n)]
        dp[0] = 1 # there is one way to reach the first step

        dp[1] = 2 # there is two ways to rach the second step by skipping the first or by going step by step

        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n-1]


s = Solution()

print(s.climbStairs(3))
