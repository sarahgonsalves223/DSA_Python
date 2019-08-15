#
# @lc app=leetcode id=250 lang=python
#
# [250] Count Univalue Subtrees
#
# https://leetcode.com/problems/count-univalue-subtrees/description/
#
# algorithms
# Medium (49.71%)
# Total Accepted:    43.6K
# Total Submissions: 87.7K
# Testcase Example:  '[5,1,5,5,5,null,5]'
#
# Given a binary tree, count the number of uni-value subtrees.
# 
# A Uni-value subtree means all nodes of the subtree have the same value.
# 
# Example :
# 
# 
# Input:  root = [5,1,5,5,5,null,5]
# 
# ⁠             5
# ⁠            / \
# ⁠           1   5
# ⁠          / \   \
# ⁠         5   5   5
# 
# Output: 4
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
    def __init__(self):
        self.counter = 0
        
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.unitree(root)
        return self.counter
    
    def unitree(self, root):
        if root == None:
            return -1
        elif root.left == None and root.right == None:
            self.counter = self.counter + 1
            return root.val
        else:
            left = self.unitree(root.left)
            right = self.unitree(root.right)
            if left == right and left == root.val:
                self.counter = self.counter + 1
                return left
            if left == -1 and right == root.val:
                self.counter = self.counter + 1
                return right
            if right == -1 and left == root.val:
                self.counter = self.counter + 1
                return left
