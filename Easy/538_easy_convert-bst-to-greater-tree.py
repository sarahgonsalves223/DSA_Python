#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (51.96%)
# Total Accepted:    88.8K
# Total Submissions: 170.8K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
# 
# 
# Example:
# 
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
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
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.convert(root, 0)
        return root
    
    def convert(self, root: TreeNode, value: int) -> TreeNode:
        if not root:
            return root
        right = self.sum(root.right)
        root.val = root.val + right + value
        self.convert(root.right, value)
        self.convert(root.left, root.val)
        return root
        
    def sum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return root.val
        left = self.sum(root.left)
        right = self.sum(root.right)
        
        sums = root.val + left + right
        return sums
        
