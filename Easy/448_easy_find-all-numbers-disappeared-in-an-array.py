#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (53.96%)
# Total Accepted:    169.4K
# Total Submissions: 313.9K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
# 
# Find all the elements of [1, n] inclusive that do not appear in this array.
# 
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]
# 
# 
#
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            num = nums[i]
            while nums[num-1] != num:
                temp = nums[num-1]
                nums[num-1] = num
                num = temp
        ans = []
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(i+1)
        return ans
