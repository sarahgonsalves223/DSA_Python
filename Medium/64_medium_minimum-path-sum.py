#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (48.15%)
# Total Accepted:    262.2K
# Total Submissions: 538.5K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Time Complexity = O(m*n)
        Space Complexity = O(m*n)
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        matrix = [[0]*len(grid[0])]*len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i-1 >= 0 and j-1 >= 0:
                    matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j]) + grid[i][j]
                elif i-1 >= 0:
                    matrix[i][j] = matrix[i-1][j] + grid[i][j]
                else:
                    matrix[i][j] = matrix[i][j-1] + grid[i][j]
        return matrix[len(grid)-1][len(grid[0])-1]
