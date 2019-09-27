#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.45%)
# Total Accepted:    814.4K
# Total Submissions: 3.2M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        """
        Space Complexity = O(1)
        Time Complexity = O(n) where n is the number of digits
        **Beware of integer overflow since they've mentioned it's a 32 bit signed integer. Therefore, anything greater that 2^31-1 will be 0.**
        """
        if x < 0:
            return -1*self.reverse(abs(x))
        num = 0
        while x > 0:
            num = num*10 + x%10
            x = x//10
        if num > 2147483647:
            return 0
        return num
