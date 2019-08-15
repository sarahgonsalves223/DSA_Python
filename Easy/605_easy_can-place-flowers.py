#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (31.19%)
# Total Accepted:    67.7K
# Total Submissions: 217.1K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# Suppose you have a long flowerbed in which some of the plots are planted and
# some are not. However, flowers cannot be planted in adjacent plots - they
# would compete for water and both would die.
# 
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means
# empty and 1 means not empty), and a number n, return if n new flowers can be
# planted in it without violating the no-adjacent-flowers rule.
# 
# Example 1:
# 
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# 
# 
# 
# Note:
# 
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.
# 
# 
#
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                if (i > 0 and flowerbed[i-1] == 0) and (i < len(flowerbed)-1 and flowerbed[i+1] == 0):
                    n = n -1
                    flowerbed[i] = 1
                elif i == 0 and (i < len(flowerbed)-1 and flowerbed[i+1] == 0):
                    n = n -1
                    flowerbed[i] = 1
                elif i == len(flowerbed)-1 and (i>0 and flowerbed[i-1] == 0):
                    n = n -1
                    flowerbed[i] = 1
                elif len(flowerbed) == 1:
                    n = n -1
                    flowerbed[i] = 1
            if n == 0:
                return True
                    
        return n == 0
                    
            
            
