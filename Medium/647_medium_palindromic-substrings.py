#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (57.68%)
# Total Accepted:    119.4K
# Total Submissions: 206K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# 
# Note:
# 
# 
# The input string length won't exceed 1000.
# 
# 
# 
# 
#
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Space Complexity = O(1)
        Time Complexity = O(n**2)
        """
        cache = {}
        total = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                isp = self.isAPalindrome(i, j, s, cache)
                if isp:
                    total += 1
        return total
    
    def isAPalindrome(self, start, end, s, cache):
        if end - start < 2:
            return True
        else:
            t = s[start:end]
            if t in cache:
                return cache[t]
            else:
                if s[start] == s[end-1]:
                    cache[t] = self.isAPalindrome(start+1, end-1, s, cache)
                else:
                    cache[t] = False
                return cache[t]

