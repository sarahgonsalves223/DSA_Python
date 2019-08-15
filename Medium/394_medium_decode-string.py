#
# @lc app=leetcode id=394 lang=python
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (45.84%)
# Total Accepted:    119K
# Total Submissions: 259.6K
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
# 
# Examples:
# 
# 
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# 
# 
# 
# 
#
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch == "]":
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop() #pop the open bracket
                num = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                final = ""
                while num > 0:
                    final = final + string
                    num = num - 1
                stack.append(final)
            else:
                stack.append(ch)
        return "".join(stack)
                
                
