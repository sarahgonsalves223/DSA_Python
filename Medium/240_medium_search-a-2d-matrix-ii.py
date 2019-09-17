#
# @lc app=leetcode id=240 lang=python
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (41.24%)
# Total Accepted:    206K
# Total Submissions: 497.6K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# Example:
# 
# Consider the following matrix:
# 
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# Given target = 5, return true.
# 
# Given target = 20, return false.
# 
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if target == matrix[row][col]:
                return True
            rowd = row
            cold = col
            if target > matrix[rowd][cold]:
                row += 1
            if target < matrix[rowd][cold]:
                col -= 1
        return False
