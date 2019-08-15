#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (37.89%)
# Total Accepted:    218.6K
# Total Submissions: 576.8K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mappie_one = {}
        mappie_two = {}
        
        for i in range(len(s)):
            if s[i] in mappie_one:
                if mappie_one[s[i]] != t[i]:
                    return False
            elif t[i] in mappie_two:
                return False
            else:
                mappie_one[s[i]] = t[i]
                mappie_two[t[i]] = s[i]
        return True
            
