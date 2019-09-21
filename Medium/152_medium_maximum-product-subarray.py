#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (29.81%)
# Total Accepted:    242K
# Total Submissions: 805.9K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(1)
        """
        if not nums:
            return 0
        pos = nums[0]
        neg = nums[0]
        cmax = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            cpos = max(num, pos*num, neg*num)
            cneg = min(num, pos*num, neg*num)
            pos = cpos
            neg = cneg
            cmax = max(cmax, pos, neg)
        return cmax
