#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (42.43%)
# Total Accepted:    240.2K
# Total Submissions: 557.8K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        max_streak = 0
        nums_set = set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                curr_streak = 0
                
                while num in nums_set:
                    curr_streak += 1
                    num += 1
                
                max_streak = max(max_streak, curr_streak)
        return max_streak
                
            
