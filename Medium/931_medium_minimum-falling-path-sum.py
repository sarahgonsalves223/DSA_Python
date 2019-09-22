#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
# https://leetcode.com/problems/minimum-falling-path-sum/description/
#
# algorithms
# Medium (59.12%)
# Total Accepted:    24.4K
# Total Submissions: 41.1K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a square array of integers A, we want the minimum sum of a falling path
# through A.
# 
# A falling path starts at any element in the first row, and chooses one
# element from each row.  The next row's choice must be in a column that is
# different from the previous row's column by at most one.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: 12
# Explanation: 
# The possible falling paths are:
# 
# 
# 
# [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
# 
# 
# The falling path with the smallest sum is [1,4,7], so the answer is 12.
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length == A[0].length <= 100
# -100 <= A[i][j] <= 100
# 
#
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        """
        Time Complexity = O(n^2)
        Space Complexity = O(n^2)
        """
        if len(A) == 0 or len(A[0]) == 0:
            return 0
        matrix = [[0]*len(A[0]) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i==0:
                    matrix[i][j] = A[i][j]
                else:
                    if j == 0:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j+1]) + A[i][j]
                    elif j == len(A)-1:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1]) + A[i][j]
                    else:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i-1][j+1]) + A[i][j]
        return min(matrix[len(A)-1])
