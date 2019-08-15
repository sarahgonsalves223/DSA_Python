#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (61.06%)
# Total Accepted:    506.6K
# Total Submissions: 829.7K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        for i in range(1, len(nums)):
            num = num ^ nums[i]
        return num
