from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sell at day ith  cannot buy at day i+1
        n = len(prices)
        dp = [0 for _ in range(n+1)]  # dp[i] maximum profit could be gained at day i 
        # before caluculation i suppose i did not do any activity yet.
        #so:
        dp[0] = 0
        for i in range(1,n+1):
            if dp[i-1] >0 : # sold on the last day  i cannot buy 
                continue
            if dp[i-1] <0 : 
                dp[i] = max(dp[i-1]+prices[i-1],0)
                continue
            dp[i] = -prices[i-1] # bought , lost money so (-)

        return dp
s = Solution()
print(s.maxProfit([1,3,4,0,4]))
        
