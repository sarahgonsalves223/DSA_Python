#
# @lc app=leetcode id=349 lang=python
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (56.11%)
# Total Accepted:    251.8K
# Total Submissions: 444.4K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# 
# 
# Note:
# 
# 
# Each element in the result must be unique.
# The result can be in any order.
# 
# 
# 
# 
#
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        settie = set(nums1)
        soln = []
        
        for num in nums2:
            if num in settie:
                soln.append(num)
                
        return set(soln)
