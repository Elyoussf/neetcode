class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1 : return nums[0]
        dp = [0 for i in range(n)]
        dp[0] = nums[0] #if there is just one house 
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return dp[n-1]
