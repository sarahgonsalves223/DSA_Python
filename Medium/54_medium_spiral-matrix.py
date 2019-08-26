#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (31.11%)
# Total Accepted:    258K
# Total Submissions: 827.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return order
        top = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        left = 0
        
        while left <= right and top <= bottom:
            #print left to right
            i = left
            while i <= right and left <= right and top <= bottom:
                order.append(matrix[top][i])
                i += 1
            top += 1
            #print top to bottom
            i = top
            while i <= bottom and left <= right and top <= bottom:
                order.append(matrix[i][right])
                i += 1
            right -= 1
            #print right to left
            i = right
            while i >= left and left <= right and top <= bottom:
                order.append(matrix[bottom][i])
                i -= 1
            bottom -= 1
            #print bottom to top
            i = bottom
            while i >= top and left <= right and top <= bottom:
                order.append(matrix[i][left])
                i -= 1
            left += 1
            
        return order
