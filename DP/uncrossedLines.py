from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        return self.func(nums1,nums2)

    def solve(self,i,j,nums1,nums2,memo):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if i <= 0 or j <= 0:
            return 0
        if nums1[i-1] == nums2[j-1]:
            memo[(i,j)] = 1 + self.solve(i-1,j-1,nums1,nums2,memo)
        else:
            memo[(i,j)] =  max(self.solve(i-1,j,nums1,nums2,memo),self.solve(i,j-1,nums1,nums2,memo)) 
        return memo[(i,j)]
    

    def func(self,nums1,nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
       
        
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[n1][n2]

s = Solution()
print(s.maxUncrossedLines([1,4,2],[1,2,4]))
        
