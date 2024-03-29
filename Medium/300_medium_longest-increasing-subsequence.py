#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (41.23%)
# Total Accepted:    277.1K
# Total Submissions: 665.8K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        if not nums or len(nums) == 0:
            return 0
        array = [1]*len(nums)
        for i in range(len(nums)):
            max_value = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_value = max(max_value, array[j]+1)
            array[i] = max_value
        return max(array)
                
                
