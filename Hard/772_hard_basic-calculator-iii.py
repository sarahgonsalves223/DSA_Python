#
# @lc app=leetcode id=772 lang=python3
#
# [772] Basic Calculator III
#
# https://leetcode.com/problems/basic-calculator-iii/description/
#
# algorithms
# Hard (42.07%)
# Total Accepted:    24.4K
# Total Submissions: 59.2K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators , open ( and closing parentheses ) and empty spaces  . The integer
# division should truncate toward zero.
# 
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2147483648, 2147483647].
# 
# Some examples:
# 
# 
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
# 
# 
# 
# 
# Note: Do not use the eval built-in library function.
# 
#
class Solution:
    def calculate(self, s: str) -> int:
        """
        PATHETIC CODE!!!!!
        Time complexity: O(n) I guess
        Space complexity: O(n) I guess
        """
        s = s.replace(" ", "")
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i].isdigit():
                num, i = self.getNumber(s, i)
                if stack:
                    if stack[-1] == "*":
                        stack.pop()
                        num1 = int(stack.pop())
                        num = str(int(num) * num1)
                    elif stack[-1] == "/":
                        stack.pop()
                        num1 = stack.pop()
                        num = str(int(num1) // int(num))
                stack.append(num)
            elif s[i] == ")":
                total = 0
                prev = 0
                while stack and stack[-1] != "(":
                    num = stack.pop()
                    if num[0] == "-" and num != "-":
                        num = int(num)
                        prev = int(num)
                        total += num
                    elif num.isdigit():
                        total += int(num)
                        prev = int(num)
                    elif num == "-":
                        total += -2*prev
                stack.pop()
                num = total
                if stack:
                    if stack[-1] == "*":
                        stack.pop()
                        num1 = int(stack.pop())
                        num = str(int(num) * num1)
                    elif stack[-1] == "/":
                        stack.pop()
                        num1 = stack.pop()
                        num = str(int(num1) // int(num))
                stack.append(str(num))
            else:
                if s[i] == "+":
                    stack.append(s[i])
                elif s[i] == "-":
                    stack.append(s[i])
                elif s[i] == "*":
                    stack.append(s[i])
                elif s[i] == "/":
                    stack.append(s[i])
                else:
                    print("should not be here!")
            i += 1
        total = self.addUp(stack)
        return total
                
    def addUp(self, stack):
        if len(stack) == 1:
            return int(stack.pop())
        print(stack)
        total = 0
        while stack:
            num = stack.pop()
            if num[0] == "-" and num != "-":
                num = int(num)
                prev = int(num)
                total += num
            elif num.isdigit():
                total += int(num)
                prev = int(num)
            elif num == "-":
                total += -2*prev
        return total
    
    def getNumber(self, s, i):
        num = ""
        while i < len(s):
            if s[i].isdigit():
                num = num + s[i]
                i += 1
            else:
                break
        return num, i-1
                
            
            
