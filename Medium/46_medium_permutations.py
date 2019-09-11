#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (56.79%)
# Total Accepted:    431.2K
# Total Submissions: 753K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        soln = []
        if len(nums) < 2:
            return [nums]
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            rest_permutes = self.permute(rest)
            for perms in rest_permutes:
                soln.append([nums[i]] + perms)
        return soln
