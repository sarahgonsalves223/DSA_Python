#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#
# https://leetcode.com/problems/arithmetic-slices/description/
#
# algorithms
# Medium (56.24%)
# Total Accepted:    69.9K
# Total Submissions: 123.8K
# Testcase Example:  '[1,2,3,4]'
#
# A sequence of number is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.
# 
# For example, these are arithmetic sequence:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# 
# The following sequence is not arithmetic. 1, 1, 2, 5, 7 
# 
# 
# A zero-indexed array A consisting of N numbers is given. A slice of that
# array is any pair of integers (P, Q) such that 0 
# 
# A slice (P, Q) of array A is called arithmetic if the sequence:
# ⁠   A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this
# means that P + 1 < Q.
# 
# The function should return the number of arithmetic slices in the array A. 
# 
# 
# Example:
# 
# A = [1, 2, 3, 4]
# 
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3,
# 4] itself.
# 
#
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """
        Space Complexity = O(1)
        Time Complexity = O(n)
        """
        if len(A) < 3:
            return 0
        i = 1
        totes = 0
        while i < len(A):
            total = 1
            diff = A[i] - A[i-1]
            while i < len(A) and A[i] - A[i-1] == diff:
                diff = A[i] - A[i-1]
                i += 1
                total += 1
            if total >=3:
                totes += self.calculate(total)
        return totes
    
    def calculate(self, total):
        i = 3
        totes = 0
        while i <= total:
            totes += total - i + 1
            i += 1
        return totes

