#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#
# https://leetcode.com/problems/number-of-atoms/description/
#
# algorithms
# Hard (45.53%)
# Total Accepted:    13.9K
# Total Submissions: 30K
# Testcase Example:  '"H2O"'
#
# Given a chemical formula (given as a string), return the count of each atom.
# 
# An atomic element always starts with an uppercase character, then zero or
# more lowercase letters, representing the name.
# 
# 1 or more digits representing the count of that element may follow if the
# count is greater than 1.  If the count is 1, no digits will follow.  For
# example, H2O and H2O2 are possible, but H1O2 is impossible.
# 
# Two formulas concatenated together produce another formula.  For example,
# H2O2He3Mg4 is also a formula.  
# 
# A formula placed in parentheses, and a count (optionally added) is also a
# formula.  For example, (H2O2) and (H2O2)3 are formulas.
# 
# Given a formula, output the count of all elements as a string in the
# following form: the first name (in sorted order), followed by its count (if
# that count is more than 1), followed by the second name (in sorted order),
# followed by its count (if that count is more than 1), and so on.
# 
# Example 1:
# 
# Input: 
# formula = "H2O"
# Output: "H2O"
# Explanation: 
# The count of elements are {'H': 2, 'O': 1}.
# 
# 
# 
# Example 2:
# 
# Input: 
# formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation: 
# The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# 
# 
# 
# Example 3:
# 
# Input: 
# formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation: 
# The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# 
# 
# 
# Note:
# All atom names consist of lowercase letters, except for the first character
# which is uppercase.
# The length of formula will be in the range [1, 1000].
# formula will only consist of letters, digits, and round parentheses, and is a
# valid formula as defined in the problem.
# 
#
from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        Happy with the much much cleaner code :D
        Time Complexity = O(n)
        Space Complexity = O(n)
        where n is the len of the formula
        """
        stack = self.removeParens(formula)
        dicti = self.convertToDict(stack)
        return self.convertDict(dicti)
    
    def removeParens(self, formula):
        stack = []
        i = 0
        while i < len(formula):
            char = formula[i]
            if char.isalpha() and not char.islower():
                element, i =  self.getElement(formula, i+1)
                element = char + element
                stack.append(element)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                num, i = self.getNextNumber(formula, i+1)
                self.getStack(stack, num)
            elif char.isdigit():
                num, i = self.getNextNumber(formula, i)
                stack.append(num)
            i += 1
        return stack
    
    def getStack(self, stack, num):
        stack2 = []
        while stack and stack[-1] != "(":
            prev = stack.pop()
            if prev.isdigit():
                curr = str(int(prev)*int(num))
                stack2.append(curr)
            else:
                if stack2 and stack2[-1].isdigit():
                    stack2.append(prev)
                else:
                    stack2.append(num)
                    stack2.append(prev)
        stack.pop()
        stack.extend(reversed(stack2))
    
    def convertToDict(self, stack):
        dicti = defaultdict(lambda:0)
        i = 0
        while i < len(stack):
            if stack[i].isalpha() and (i + 1) < len(stack) and stack[i+1].isdigit():
                dicti[stack[i]] = dicti[stack[i]] + int(stack[i+1])
                i += 2
            else:
                dicti[stack[i]] = dicti[stack[i]] + 1
                i += 1
        return dicti 
    
    def convertDict(self, dicti):
        keys = dicti.keys()
        ans = ""
        for key in sorted(keys):
            if dicti[key] > 1:
                ans += key + str(dicti[key])
            else:
                ans += key
        return ans
        
    def getNextNumber(self, formula, i):
        num = ""
        while i < len(formula):
            if formula[i].isdigit():
                num += formula[i]
                i += 1
            else:
                break
        return "1" if not num.isdigit() else num, i-1
        
    def getElement(self, formula, i):
        rest = ""
        while i < len(formula):
            if formula[i].islower():
                rest += formula[i]
                i += 1
            else:
                break
            
        return rest, i-1

