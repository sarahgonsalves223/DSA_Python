#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (52.07%)
# Total Accepted:    285.3K
# Total Submissions: 547.9K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = self.helper(nums, 0, len(nums)-1)
        return root
    
    def helper(self, nums: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None
        mid = int((start+end)/2)
        print(mid)
        node = TreeNode(nums[mid])
        left = self.helper(nums, start, mid-1)
        right = self.helper(nums, mid+1, end)
        node.left = left
        node.right = right
        return node
