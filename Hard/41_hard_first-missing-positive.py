#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (29.49%)
# Total Accepted:    259.1K
# Total Submissions: 859.1K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Time complexity = O(n)
        Space complexity = O(1)
        """
        if len(nums) < 1:
            return 1
        i = 0
        while i < len(nums):
            while nums[i] >= 1 and nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                extra = nums[nums[i]-1] 
                nums[nums[i]-1] = nums[i]
                nums[i] = extra
            i += 1
    
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i+1
        return len(nums)+1
