#
# @lc app=leetcode id=224 lang=python
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (33.63%)
# Total Accepted:    121.8K
# Total Submissions: 358.8K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
# 
# Example 1:
# 
# 
# Input: "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: " 2-1 + 2 "
# Output: 3
# 
# Example 3:
# 
# 
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# 
#
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ""
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                stack.append(num)
            elif s[i] == "(":
                stack.append(s[i])
                i += 1
            elif s[i] == ")":
                num = stack.pop()
                stack.pop() # remove the open paren
                if len(stack) > 0 and (stack[-1] == "+" or stack[-1] == "-"):
                    op = stack.pop()
                    num2 = stack.pop()
                    if op == "+":
                        stack.append(int(num) + int(num2))
                    else:
                        stack.append(int(num2) - int(num))
                else:
                    stack.append(num)
                i += 1
            else:
                op = s[i]
                if s[i+1].isdigit():
                    num = stack.pop()
                    num2 = ""
                    i += 1
                    while i < len(s) and s[i].isdigit():
                        num2 += s[i]
                        i += 1
                    if op == "+":
                        stack.append(int(num) + int(num2))
                    else:
                        stack.append(int(num) - int(num2))
                else:
                    stack.append(s[i])
                    i += 1
                    continue
        return int(stack.pop())
            
