#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (34.24%)
# Total Accepted:    142.3K
# Total Submissions: 405.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
# 
# 
#
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        m = len of rows
        n = len of colums
        Time Complexity = O(m*n)
        Space Complexity = O(n)
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        dp = [0]*len(matrix[0])
        max_rect = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[j] = dp[j] + 1
                else:
                    dp[j] = 0
            area = self.largestRectangleArea(dp)
            max_rect = max(max_rect, area)
        return max_rect
        
        
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        stack = [-1]
        i = 0
        max_width = 0
        while i < len(heights):
            if stack[-1] != -1:
                if heights[i] >= heights[stack[-1]]:
                    stack.append(i)
                else:
                    while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                        index = stack.pop()
                        width = heights[index] * (i-1 - stack[-1])
                        max_width = max(max_width, width)
                    stack.append(i)
            else:
                stack.append(i)
            i += 1
        
        if stack[-1] != -1:
            while stack[-1] != -1:
                index = stack.pop()
                width = heights[index] * (i - 1 - stack[-1])
                max_width = max(max_width, width)
        
        return max_width
