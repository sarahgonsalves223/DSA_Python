#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (39.99%)
# Total Accepted:    158.5K
# Total Submissions: 387.1K
# Testcase Example:  '"()())()"'
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
# 
# Note: The input string may contain letters other than the parentheses ( and
# ).
# 
# Example 1:
# 
# 
# Input: "()())()"
# Output: ["()()()", "(())()"]
# 
# 
# Example 2:
# 
# 
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# 
# 
# Example 3:
# 
# 
# Input: ")("
# Output: [""]
# 
#
class Solution:
    def __init__(self):
        self.min_rem = float('inf')
        self.ans = set()
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.remove(s, 0, 0, 0, [], 0)
        return self.ans
    
    def remove(self, s, index, left, right, curr, rem):
        if index == len(s):
            if left == right:
                string = "".join(curr)
                if rem <= self.min_rem:
                    if rem < self.min_rem:
                        self.ans = set()
                        self.min_rem = rem
                    self.ans.add(string)
        else:
            ch = s[index]
            if ch != "(" and ch != ")":
                curr.append(ch)
                self.remove(s, index+1, left, right, curr, rem)
                curr.pop()
            else:
                self.remove(s, index+1, left, right, curr, rem+1)
                if ch == "(":
                    curr.append(ch)
                    self.remove(s, index+1, left+1, right, curr, rem)
                    curr.pop()
                else:
                    if left > right:
                        curr.append(ch)
                        self.remove(s, index+1, left, right+1, curr, rem)
                        curr.pop()

