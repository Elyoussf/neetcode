from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        return self.solve(len(nums1),len(nums2),nums1,nums2,{})

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
