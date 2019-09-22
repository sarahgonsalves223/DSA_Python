#
# @lc app=leetcode id=1055 lang=python3
#
# [1055] Shortest Way to Form String
#
# https://leetcode.com/problems/shortest-way-to-form-string/description/
#
# algorithms
# Medium (58.69%)
# Total Accepted:    6.5K
# Total Submissions: 11.1K
# Testcase Example:  '"abc"\n"abcbc"'
#
# From any string, we can form a subsequence of that string by deleting some
# number of characters (possibly no deletions).
# 
# Given two strings source and target, return the minimum number of
# subsequences of source such that their concatenation equals target. If the
# task is impossible, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: source = "abc", target = "abcbc"
# Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are
# subsequences of source "abc".
# 
# 
# Example 2:
# 
# 
# Input: source = "abc", target = "acdbc"
# Output: -1
# Explanation: The target string cannot be constructed from the subsequences of
# source string due to the character "d" in target string.
# 
# 
# Example 3:
# 
# 
# Input: source = "xyz", target = "xzyxz"
# Output: 3
# Explanation: The target string can be constructed as follows "xz" + "y" +
# "xz".
# 
# 
# Constraints:
# 
# 
# Both the source and target strings consist of only lowercase English letters
# from "a"-"z".
# The lengths of source and target string are between 1 and 1000.
# 
#
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
        Space Complexity = O(1)
        Time Complexity = O(m*n)
        m = len(source)
        n = len(target)
        """
        chrs = set(source)
        total = 0
        j = 0
        for i in range(len(target)):
            if target[i] in chrs:
                while source[j] != target[i]:
                    j += 1
                    if j == len(source):
                        j = 0
                        total += 1
                j += 1
                if j == len(source):
                    j = 0
                    total += 1
            else:
                return -1
        if j < len(source) and j>0:
            total += 1
        return total
