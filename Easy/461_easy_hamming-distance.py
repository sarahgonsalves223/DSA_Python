#
# @lc app=leetcode id=461 lang=python
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (70.58%)
# Total Accepted:    253.3K
# Total Submissions: 358.8K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given two integers x and y, calculate the Hamming distance.
# 
# Note:
# 0 ≤ x, y < 231.
# 
# 
# Example:
# 
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# 
# The above arrows point to positions where the corresponding bits are
# different.
# 
# 
#
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = x^y
        count = 0
        while x:
            count += x & 1
            x >>= 1
        return count
