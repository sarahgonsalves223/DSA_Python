#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (42.97%)
# Total Accepted:    261K
# Total Submissions: 591.4K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#
class Solution:
    def __init__(self):
        self.ans = []
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time Complexity = O(n^2)
        Think of it as a tree where every element visits all the remaining so 
        n-1, n-2, n-3 .....0. 
        This is basically summation of 0 to n-1, which is n*(n+1)/2 = n^2
        """
        candidates.sort()
        self.find(candidates, 0, target, [])
        return self.ans
        
    def find(self, candidates, index, target, curr):
        if target < 0:
            return
        elif target == 0:
            self.ans.append(curr)
        else:
            for i in range(index, len(candidates)):
                """
                This condition is tricky. i>0 does not work because you want 
                to always get the first element of every iteration and then 
                start skipping similar elements. Basically every curr 
                (the current combination) should always contain the first 
                element that it starts the iteration from since that's unique.
                After that you can skip all the same elements that are already in curr.
                """
                if i>index and candidates[i] == candidates[i-1]:
                    continue
                self.find(candidates, i+1, target-candidates[i], curr + [candidates[i]])
        
