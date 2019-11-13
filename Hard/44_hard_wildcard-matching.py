#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (23.22%)
# Total Accepted:    204.8K
# Total Submissions: 866.6K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*'.
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# ? or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
# 
# 
# Example 4:
# 
# 
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
# 
# 
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Time complexity = O(len(s)*len(p))
        Space complexity = O(len(s)*len(p))
        """
        dp = [[False]*(len(s)+1) for i in range(len(p)+1)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if j == 0:
                    if i == 0:
                        dp[i][j] = True
                    else:
                        if p[i-1] == "*":
                            dp[i][j] = dp[i-1][j]
                        else:
                            dp[i][j] = False
                else:
                    if i == 0:
                        dp[i][j] = False
                    else:
                        if p[i-1] == "*":
                            dp[i][j] = dp[i-1][j] or dp[i][j-1]
                        elif p[i-1] == "?":
                            dp[i][j] = dp[i-1][j-1]
                        else:
                            if p[i-1] == s[j-1]:
                                dp[i][j] = dp[i-1][j-1]
                            else:
                                dp[i][j] = False
        return dp[i][j]
