#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (33.80%)
# Total Accepted:    162.8K
# Total Submissions: 471.1K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Time Complexity = O(m*n)
        Space Complexity = O(m)
        """
        if len(matrix) == 0:
            return 0
        dp = [0]*len(matrix[0])
        maxi = 0
        for i in range(len(matrix)):
            curr = [0]*len(matrix[0])
            for j in range(len(matrix[0])):
                if matrix[i][j] != "1":
                    continue
                curr[j] = min(min(dp[j], curr[j-1]), dp[j-1]) + 1
                maxi = max(maxi, curr[j]**2)
            dp = curr
        return maxi
                
                    
