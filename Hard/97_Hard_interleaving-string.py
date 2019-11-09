#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (28.64%)
# Total Accepted:    127.1K
# Total Submissions: 433.2K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
# 
# Example 1:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# 
# 
#
class Solution:
    def __init__(self):
        self.memoize = {}
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time Complexity = O(m*n)
        Space Complexity = O(m*n*(m+n))
        """
        if len(s1) + len(s2) != len(s3):
            return False
        return self.inter(s1, 0, s2, 0, s3, 0)
    
    def inter(self, s1, i, s2, j, s3, k):
        if (i,j,k) in self.memoize:
            return self.memoize[(i,j,k)]
        one = s1[i:]
        two = s2[j:]
        three = s3[k:]
        if three and not (one or two):
            return False
        if one == "" and two == "" and three == "":
            return True
        one1 = False
        two2 = False
        if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
            one1 = self.inter(s1, i+1, s2, j, s3, k+1)
        if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
            two2 = self.inter(s1, i, s2, j+1, s3, k+1)
        self.memoize[(i,j,k)] = one1 or two2
        return one1 or two2
