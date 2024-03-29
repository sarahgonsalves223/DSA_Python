#
# @lc app=leetcode id=617 lang=python
#
# [617] Merge Two Binary Trees
#
# https://leetcode.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (70.89%)
# Total Accepted:    197.4K
# Total Submissions: 278.5K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# Given two binary trees and imagine that when you put one of them to cover the
# other, some nodes of the two trees are overlapped while the others are not.
# 
# You need to merge them into a new binary tree. The merge rule is that if two
# nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.
# 
# Example 1:
# 
# 
# Input: 
# Tree 1                     Tree 2                  
# ⁠         1                         2                             
# ⁠        / \                       / \                            
# ⁠       3   2                     1   3                        
# ⁠      /                           \   \                      
# ⁠     5                             4   7                  
# Output: 
# Merged tree:
# 3
# / \
# 4   5
# / \   \ 
# 5   4   7
# 
# 
# 
# 
# Note: The merging process must start from the root nodes of both trees.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.helper(t1, t2)
    
    def helper(self, t1, t2):
        
        total = 0
        if t1 is not None:
            total = total + t1.val
        if t2 is not None:
            total = total + t2.val
        if t1 is not None or t2 is not None:
            t3 = TreeNode(total)
            if t1 is not None:
                left1 = t1.left
                right1 = t1.right
            else:
                left1 = None
                right1 = None
            if t2 is not None:
                left2 = t2.left
                right2 = t2.right
            else:
                left2 = None
                right2 = None
            t3.left = self.helper(left1, left2)
            t3.right = self.helper(right1, right2)
            return t3
        return None    
