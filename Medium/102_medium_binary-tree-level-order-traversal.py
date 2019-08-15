#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (49.62%)
# Total Accepted:    413.9K
# Total Submissions: 834.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        outer = []
        if not root:
            return queue
        queue.append(root)
        while len(queue) > 0:
            q2 = []
            inner = []
            while len(queue) > 0:
                node = queue.pop(0)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
                inner.append(node.val)
            queue = q2
            outer.append(inner)
        return outer
            
            
            
        
