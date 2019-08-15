#
# @lc app=leetcode id=897 lang=python
#
# [897] Increasing Order Search Tree
#
# https://leetcode.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (65.62%)
# Total Accepted:    37.9K
# Total Submissions: 57.7K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# Given a binary search tree, rearrange the tree in in-order so that the
# leftmost node in the tree is now the root of the tree, and every node has no
# left child and only 1 right child.
# 
# 
# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 
# ⁠      5
# ⁠     / \
# ⁠   3    6
# ⁠  / \    \
# ⁠ 2   4    8
# /        / \ 
# 1        7   9
# 
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 
# ⁠1
# \
# 2
# \
# 3
# \
# 4
# \
# 5
# \
# 6
# \
# 7
# \
# 8
# \
# ⁠                9  
# 
# Note:
# 
# 
# The number of nodes in the given tree will be between 1 and 100.
# Each node will have a unique integer value from 0 to 1000.
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
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        traversal = self.inorder(root, [])
        root = TreeNode(-1)
        prev = root
        for node in traversal:
            node.left = None
            node.right = None
            prev.right = node
            prev = node
        return root.right      
    
    def inorder(self, root, traversal):
        if root:
            traversal = self.inorder(root.left, traversal)
            traversal.append(root)
            traversal = self.inorder(root.right, traversal)
        return traversal
