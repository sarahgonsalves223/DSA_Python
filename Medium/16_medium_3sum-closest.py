#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.78%)
# Total Accepted:    381.3K
# Total Submissions: 833.5K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        ans = -1
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            total = 0
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target - total) < diff:
                    diff = abs(target - total)
                    ans = total
                if total == target:
                    return target 
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return ans
