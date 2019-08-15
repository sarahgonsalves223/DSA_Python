#
# @lc app=leetcode id=404 lang=python
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (49.50%)
# Total Accepted:    135K
# Total Submissions: 272.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, False)
        
    def helper(self, root, isLeft):
        if not root:
            return 0
        if root.left == None and root.right == None:
            if isLeft:
                return root.val
            return 0
        sumLeft = self.helper(root.left, True)
        sumRight = self.helper(root.right, False)
        return sumLeft + sumRight
        
        
            
