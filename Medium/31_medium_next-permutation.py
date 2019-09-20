#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (30.91%)
# Total Accepted:    271.5K
# Total Submissions: 874.1K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #[3,2,7,3,9,5,4,3,2,1]
        i = len(nums) - 1
        while i>0 and nums[i] <= nums[i-1]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        else:
            j = i-1
            while i<len(nums) and nums[i] > nums[j]:
                i+=1
            i = i-1
            nums[j], nums[i] = nums[i], nums[j]
            nums[j+1:] = sorted(nums[j+1:])
            return
        
