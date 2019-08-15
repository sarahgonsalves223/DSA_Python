#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (48.96%)
# Total Accepted:    183.7K
# Total Submissions: 375.2K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        q = deque([])
        if root:
            q.append(root)
        while len(q) > 0:
            level = deque([])
            while len(q) > 0:
                node = q.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            q = level
            ans.append(node.val)
        return ans
