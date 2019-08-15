#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (42.74%)
# Total Accepted:    240.5K
# Total Submissions: 562.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        levels = []
        q = deque([])
        if root:
            q.append(root)
        flag = False
        while len(q) > 0:
            inner = deque([])
            inner_level = []
            while len(q) > 0:
                node = q.popleft()
                if node.left:
                    inner.append(node.left)
                if node.right:
                    inner.append(node.right)
                inner_level.append(node.val)
            q = inner
            if flag:
                inner_level.reverse()
            flag = not flag
            levels.append(inner_level)
        return levels
        
