from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if (n==0 or n==1) :
            return 0

        dp = [0 for i in range(n)] # dp[i] means the minimum effort to reach (i+1)th stair (O-based index)
        
        for i in range(2,n):
            dp[i]+= min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return min(dp[n-1]+cost[n-1],dp[n-2]+cost[n-2])
s = Solution()

cost = [1,2,1,2,1,1,1]
print(s.minCostClimbingStairs(cost))
    
