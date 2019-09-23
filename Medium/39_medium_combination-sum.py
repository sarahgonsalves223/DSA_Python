#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (50.13%)
# Total Accepted:    397K
# Total Submissions: 781.3K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#
from collections import defaultdict
class Solution:
    def __init__(self):
        self.ans = []
        self.candidates = None
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Space Complexity = O(1) -> No extra space apart from the soln
        Time Complexity = O(target*len(candidates))
        """
        candidates.sort()
        self.candidates = candidates
        self.find(target, [], 0)
        return self.ans
        
    def find(self, target, curr, index):
        if target == 0:
            self.ans.append(curr)
            return
        for i in range(index, len(self.candidates)):
            if self.candidates[i] > target:
                break
            self.find(target-self.candidates[i], curr + [self.candidates[i]], i)
