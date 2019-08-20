#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (24.56%)
# Total Accepted:    616.3K
# Total Submissions: 2.5M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        soln = []
        for i in range(len(nums)-2):
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            while j<k:
                sumi = nums[i] + nums[j] + nums[k]
                if sumi == 0:
                    soln.append([nums[i],nums[j],nums[k]])
                    while j+1 < len(nums)-1 and nums[j+1] == nums[j]:
                        j += 1
                    while k-1 > j and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sumi < 0:
                    j += 1
                elif sumi > 0:
                    k -= 1
        return soln
