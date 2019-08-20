#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (54.44%)
# Total Accepted:    400.8K
# Total Submissions: 736.2K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            self.add(num, subsets)
        return subsets
        
    def add(self, num: int, subsets: List[int]):
        new_subsets = []
        for subset in subsets:
            new_subset = copy.deepcopy(subset)
            new_subset.append(num)
            new_subsets.append(new_subset)
        subsets.extend(new_subsets)
            
        
