#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (40.71%)
# Total Accepted:    109.4K
# Total Submissions: 264.1K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
# 
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
# 
# Example 1:
# 
# 
# Input: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
#
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Time Complexity = O(mn)
        Space Complexity = O(mn)
        """
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for j in range(n)]
        max_len = 0
        for i in range(n):
            for j in range(m):
                max_len = max(max_len, self.findLength(i,j, dp, matrix))
        return max_len
        
    def findLength(self, i, j, dp, matrix):
        if dp[i][j] != 0:
            return dp[i][j]
        curr = 0
        n = len(matrix)
        m = len(matrix[0])
        if j < m-1 and matrix[i][j] < matrix[i][j+1]:
            curr = max(curr, self.findLength(i, j+1, dp, matrix))
        if j > 0 and matrix[i][j] < matrix[i][j-1]:
            curr = max(curr, self.findLength(i, j-1, dp, matrix))
        if i > 0 and matrix[i][j] < matrix[i-1][j]:
            curr = max(curr, self.findLength(i-1, j, dp, matrix))
        if i < n-1 and matrix[i][j] < matrix[i+1][j]:
            curr = max(curr, self.findLength(i+1, j, dp, matrix))
        dp[i][j] = curr+1
        return dp[i][j]
            
