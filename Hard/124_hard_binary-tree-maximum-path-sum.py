#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (30.66%)
# Total Accepted:    242.1K
# Total Submissions: 768.5K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        Time Complexity = O(n)
        Space Complexity = O(log(n)) but can be O(n) if the tree is skewed
        """
        def helper(root):
            nonlocal maxi
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            one = left + root.val
            two = right + root.val
            three = right + left + root.val
            maxi = max(max(max(maxi, one), max(two, three)), root.val)
            return max(max(root.val + left, root.val), root.val + right)
        
        maxi = float('-inf')
        helper(root)
        return maxi
        
