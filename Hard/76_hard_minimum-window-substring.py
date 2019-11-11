#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (31.63%)
# Total Accepted:    296.3K
# Total Submissions: 913.2K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#
from collections import defaultdict, Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        Time Complexity: O(S + T)
        Space Complexity: O(S + T)
        """
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = Counter(t)
        required = len(count)
        formed = 0
        left = 0
        right = 0
        present = {}
        mini = len(s)
        ans = ""
        while right < len(s):
            while formed < required and right < len(s):
                if s[right] in count:
                    if s[right] in present:
                        present[s[right]] = present[s[right]] + 1
                    else:
                        present[s[right]] = 1
                    if present[s[right]] == count[s[right]]:
                        formed += 1
                right += 1
            while left < right:
                if formed == required:
                    if right-left <= mini:
                        mini = right-left
                        ans = s[left:right]
                if s[left] in present:
                    present[s[left]] = present[s[left]] - 1
                    if present[s[left]] < count[s[left]]:
                        formed -= 1
                left += 1
                if formed < required:
                    break
        return ans

