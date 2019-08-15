#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (56.05%)
# Total Accepted:    287.3K
# Total Submissions: 512.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_mult = []
        mult = 1
        for num in nums:
            left_mult.append(mult)
            mult = mult*num
        mult = 1
        right_mult = []
        for i,num in enumerate(nums[::-1]):
            nums[len(nums)-i-1] = mult*left_mult[len(nums)-i-1]
            mult = mult*num
        return nums
            
            
