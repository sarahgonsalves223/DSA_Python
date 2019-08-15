#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (57.87%)
# Total Accepted:    504.9K
# Total Submissions: 872.4K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.helperIterative(root)
        
    def helperRecurse(self, root, trav):
        if root != None:
            self.helper(root.left, trav)
            trav.append(root.val)
            self.helper(root.right, trav)
        return trav
    
    def helperIterative(self, root):
        stack = []
        trav = []
        if root != None:
            stack.append(root)
        visited = set()
        while len(stack) > 0:
            node = stack.pop()
            if node in visited:
                trav.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                visited.add(node)
        return trav
            
