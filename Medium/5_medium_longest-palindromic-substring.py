#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.75%)
# Total Accepted:    664.3K
# Total Submissions: 2.4M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Space Complexity = O(1)
        Time Complexity = O(n**2)
        """
        if len(s) < 2:
            return s
        maxi = ""
        for i in range(len(s)):
            curr = self.expand(s, i)
            maxi = curr if len(curr) > len(maxi) else maxi
        return maxi
    
    def expand(self, s, i):
        around_center = self.check(s, i, i)
        normal = self.check(s, i, i+1)
        return around_center if len(around_center) >= len(normal) else normal
    
    def check(self, s, left, right):
        if left < 0 or right >= len(s):
            return ""
        if s[left] != s[right]:
            return ""
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        st = s[left+1:right]
        return st
