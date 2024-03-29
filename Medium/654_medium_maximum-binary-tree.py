#
# @lc app=leetcode id=654 lang=python
#
# [654] Maximum Binary Tree
#
# https://leetcode.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (76.79%)
# Total Accepted:    92.9K
# Total Submissions: 121K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 
# Given an integer array with no duplicates. A maximum tree building on this
# array is defined as follow:
# 
# The root is the maximum number in the array. 
# The left subtree is the maximum tree constructed from left part subarray
# divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray
# divided by the maximum number. 
# 
# 
# 
# 
# Construct the maximum tree by the given array and output the root node of
# this tree.
# 
# 
# Example 1:
# 
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
# 
# ⁠     6
# ⁠   /   \
# ⁠  3     5
# ⁠   \    / 
# ⁠    2  0   
# ⁠      \
# ⁠       1
# 
# 
# 
# Note:
# 
# The size of the given array will be in the range [1,1000].
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.constructMax(nums, 0, len(nums)-1)
        return root
    
    def constructMax(self, nums, l, r):
        index, maxi = self.findMax(nums, l, r)
        if index != -1:
            root = TreeNode(maxi)
            root.left = self.constructMax(nums, l, index-1)
            root.right = self.constructMax(nums, index+1, r)
        else:
            root = None
        return root
        
    def findMax(self, nums, l, r):
        if l>r:
            return -1,-1
        maxi = float('-inf')
        index = -1
        for i in range(l,r+1):
            num = nums[i]
            if num > maxi:
                maxi = num
                index = i
        return index, maxi
