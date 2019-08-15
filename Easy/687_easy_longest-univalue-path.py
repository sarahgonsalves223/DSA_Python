#
# @lc app=leetcode id=687 lang=python
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (34.27%)
# Total Accepted:    64.6K
# Total Submissions: 188.4K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
# 
# The length of path between two nodes is represented by the number of edges
# between them.
# 
# 
# 
# Example 1:
# 
# Input:
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input:
# 
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# Output: 2
# 
# 
# 
# Note: The given binary tree has not more than 10000 nodes. The height of the
# tree is not more than 1000.
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
        self.longest = float('-inf')
        
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.longest
        
    def helper(self, root):
        if root == None:
            if self.longest < 0:
                self.longest = 0
            return -1
        elif root.left == None and root.right == None:
            if self.longest < 0:
                self.longest = 0
            return 0
        else:
            left = self.helper(root.left)
            right = self.helper(root.right)
            if left != -1 and right != -1:
                if root.left.val == root.right.val and root.right.val == root.val:
                    total = left + right + 2
                    if total > self.longest:
                        self.longest = total
                    return max(left, right) + 1
            if left != -1:
                if root.left.val == root.val:
                    total = left + 1
                    if total > self.longest:
                        self.longest = total
                    return total
            if right != -1:
                if root.right.val == root.val:
                    total = right + 1
                    if total > self.longest:
                        self.longest = total
                    return total
            return 0
                
