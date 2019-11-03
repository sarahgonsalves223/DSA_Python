#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (35.52%)
# Total Accepted:    135.8K
# Total Submissions: 380.3K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(1)
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        return max(self.robIndex(nums, 0, len(nums)-2), self.robIndex(nums, 1, len(nums)-1))
    
    def robIndex(self, nums, start, end):
        prev = now = 0
        for i in range(start, end+1):
            take = nums[i] + prev
            dont = now
            prev = now
            now = max(take, dont)
        return now
        
