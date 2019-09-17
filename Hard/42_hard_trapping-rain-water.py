#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (44.23%)
# Total Accepted:    344K
# Total Submissions: 769.7K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int] 
        :rtype: int
        """
        left = [-1]
        right = [-1]
        
        for h in height:
            left.append(max(left[-1], h))
        left = left[:-1]
        
        for h in reversed(height):
            right.append(max(right[-1], h))
        right = right[:-1]
        right.reverse()
        
        ans = 0
        for i,h in enumerate(height):
            if h < left[i] and h < right[i]:
                ans += min(left[i], right[i]) - h
        return ans
