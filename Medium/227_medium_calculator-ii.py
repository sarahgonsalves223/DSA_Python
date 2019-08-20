#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (34.22%)
# Total Accepted:    122.2K
# Total Submissions: 356.9K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
# 
# Example 1:
# 
# 
# Input: "3+2*2"
# Output: 7
# 
# 
# Example 2:
# 
# 
# Input: " 3/2 "
# Output: 1
# 
# Example 3:
# 
# 
# Input: " 3+5 / 2 "
# Output: 5
# 
# 
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# 
#
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        i = 0
        total = 0
        while i < len(s):
            if i < len(s) and s[i].isdigit():
                val1, i = self.getNext(s, i)
                stack.append(val1)
            else:
                op = s[i]
                i += 1
                if op == "*":
                    val1 = stack.pop()
                    val2, i = self.getNext(s, i)
                    ans = int(val1*val2)
                    stack.append(ans)
                elif op == "/":
                    val1 = stack.pop()
                    val2, i = self.getNext(s, i)
                    ans = int(val1/val2)
                    stack.append(ans)
                else:
                    stack.append(op)
        i = 0
        add = True
        while i < len(stack):
            val1 = stack[i]
            if val1 != "+" and val1 != "-":
                if add:
                    total += val1
                else:
                    total -= val1
            else:
                add = val1 == "+"
            i += 1
        return total
    
    def getNext(self, s, i):
        val = ""
        while i < len(s) and s[i].isdigit():
            val += s[i]
            i += 1
        return int(val), i
