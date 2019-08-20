#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (50.50%)
# Total Accepted:    303.1K
# Total Submissions: 600.1K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i,l in enumerate(s):
            if counts[l] == 1:
                return i
        return -1
