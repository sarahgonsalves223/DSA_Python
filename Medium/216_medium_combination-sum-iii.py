#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (52.60%)
# Total Accepted:    139.4K
# Total Submissions: 260.4K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]
        ans = []
        self.find(candidates, 0, k, n, ans, [])
        return ans
    
    def find(self, candidates, index, k, n, ans, curr):
        if n < 0 or k < 0:
            return
        elif n == 0 and k == 0:
            ans.append(curr)
        else:
            for i in range(index, len(candidates)):
                self.find(candidates, i+1, k-1, n-candidates[i], ans, curr + [candidates[i]])
        return
    
    
