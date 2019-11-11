#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (46.94%)
# Total Accepted:    44.1K
# Total Submissions: 92.4K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
# 
# Example 1:
# 
# 
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
# 
# 
#
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        Time Complexity = O(m*n)
        Space Complexity = O(min(m,n))
        """
        A, B = self.swapArrays(A, B)
        prev = [0]*(len(A)+1)
        maxi = 0
        for i in range(len(B)):
            curr = [0]*(len(A)+1)
            for j in range(len(A)):
                if A[j] == B[i]:
                    curr[j+1] = prev[j] + 1
                maxi = max(maxi, curr[j+1])
            prev = curr
        return maxi
    
    def swapArrays(self, A, B):
        if len(A) <= len(B):
            return A, B
        else:
            return B, A

