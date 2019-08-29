#
# @lc app=leetcode id=384 lang=python
#
# [384] Shuffle an Array
#
# https://leetcode.com/problems/shuffle-an-array/description/
#
# algorithms
# Medium (50.65%)
# Total Accepted:    86.1K
# Total Submissions: 169.9K
# Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
#
# Shuffle a set of numbers without duplicates.
# 
# 
# Example:
# 
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
# 
# // Shuffle the array [1,2,3] and return its result. Any permutation of
# [1,2,3] must equally likely to be returned.
# solution.shuffle();
# 
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
# 
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
# 
# 
#
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        dup = list(self.nums)
        for i in range(len(self.nums)):
            swp_index = random.randint(i, len(self.nums)-1)
            dup[i], dup[swp_index] = dup[swp_index], dup[i]
        return dup
            
            

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
