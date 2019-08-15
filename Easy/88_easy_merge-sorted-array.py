#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (36.49%)
# Total Accepted:    398.3K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return nums1
        index = len(nums1)-1
        while index >=0:
            if m>0 and nums1[m-1] > nums2[n-1]:
                nums1[index] = nums1[m-1]
                m = m - 1
            elif n > 0:
                nums1[index] = nums2[n-1]
                n = n - 1
            index = index - 1
        return nums1
