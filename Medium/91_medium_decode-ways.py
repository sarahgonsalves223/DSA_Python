#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (22.72%)
# Total Accepted:    310K
# Total Submissions: 1.3M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(1)
        """
        nums = set([str(i) for i in range(1, 27)])
        for i in range(len(s)):
            if i > 0:
                one = s[i]
                two = s[i-1:i+1]
                val = 0
                if one not in nums and two not in nums:
                    return 0
                if one in nums:
                    val += curr
                if two in nums:
                    val += prev
                prev = curr
                curr = val
            else:
                if s[i] not in nums:
                    return 0
                else:
                    prev = 1
                    curr = 1
        return curr
            
        
