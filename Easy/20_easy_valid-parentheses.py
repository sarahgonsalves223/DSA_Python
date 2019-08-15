#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.03%)
# Total Accepted:    661.4K
# Total Submissions: 1.8M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        paren_map = {")": "(", "}":"{", "]":"["}
        paren_stack = []
        for paren in s:
            if paren in paren_map:
                if len(paren_stack) > 0 and paren_stack[-1] == paren_map[paren]:
                    paren_stack.pop()
                else:
                    return False
            else:
                paren_stack.append(paren)
        if len(paren_stack) > 0:
            return False
        return True
                
        
