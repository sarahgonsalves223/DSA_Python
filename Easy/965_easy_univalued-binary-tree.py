#
# @lc app=leetcode id=965 lang=python
#
# [965] Univalued Binary Tree
#
# https://leetcode.com/problems/univalued-binary-tree/description/
#
# algorithms
# Easy (66.95%)
# Total Accepted:    43.4K
# Total Submissions: 64.8K
# Testcase Example:  '[1,1,1,1,1,null,1]'
#
# A binary tree is univalued if every node in the tree has the same value.
# 
# Return true if and only if the given tree is univalued.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,1,1,1,null,1]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [2,2,2,5,2]
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given tree will be in the range [1, 100].
# Each node's value will be an integer in the range [0, 99].
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
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.dfs(root, root.val)
        return False
            
    def dfs(self, root, value):
        if root:
            if root.val != value:
                return False
            else:
                return self.dfs(root.left, value) and self.dfs(root.right, value)
        return True
        
