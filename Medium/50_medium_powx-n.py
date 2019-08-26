#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (28.41%)
# Total Accepted:    350.5K
# Total Submissions: 1.2M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (xn).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]
# 
# 
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        multi = self.mult(abs(x), abs(n))
        if n < 0:
            multi = 1/multi
        if n%2 != 0 and x < 0:
            return -1*multi
        return multi
    
    def mult(self, x, n):
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        else:
            multi = self.mult(x, n//2)
            if n%2 == 0:
                multi = multi*multi
                return multi
            else:
                multi = x*multi*multi
                return multi
        
        
