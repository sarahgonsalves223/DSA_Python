#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (56.46%)
# Total Accepted:    376.5K
# Total Submissions: 666.9K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generate(n, n, ans, "")
        return ans
        
    def generate(self, left: int, right: int, ans: List[str], curr: str):
        if right == 0 and left == 0:
            ans.append(curr)
            return
        else:
            #if left parens are left to be used then use them up first
            if left > 0:
                self.generate(left-1, right, ans, curr + "(")
            #if right parens are more than left and zero then use right
            if right > 0 and left < right:
                self.generate(left, right-1, ans, curr + ")")
    
