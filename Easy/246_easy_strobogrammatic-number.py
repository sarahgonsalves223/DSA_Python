#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#
# https://leetcode.com/problems/strobogrammatic-number/description/
#
# algorithms
# Easy (42.81%)
# Total Accepted:    57.2K
# Total Submissions: 133.6K
# Testcase Example:  '"69"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# 
# Write a function to determine if a number is strobogrammatic. The number is
# represented as a string.
# 
# Example 1:
# 
# 
# Input:  "69"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:  "88"
# Output: true
# 
# Example 3:
# 
# 
# Input:  "962"
# Output: false
# 
#
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        """
        6 -> 9
        9 -> 6
        8 -> 8
        """
        strobo = {"6":"9", "9":"6", "8":"8", "1":"1", "0":"0"}
        ans = []
        for i in range(0,int(len(num)/2)+1):
            if num[i] in strobo:
                if strobo[num[i]] == num[len(num) - 1 - i]:
                    continue
            return False
        return True
