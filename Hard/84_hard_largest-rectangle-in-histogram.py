#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (31.97%)
# Total Accepted:    206.4K
# Total Submissions: 630.9K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#
class Solution:
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
