#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (41.71%)
# Total Accepted:    248.3K
# Total Submissions: 595.3K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \    / \
# 7    2  5   1
# 
# 
# Return:
# 
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
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

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []
        self.path(root, sum, paths, [])
        return paths
        
    def path(self, root, sum, paths, path):
        if root == None:
            return
        else:
            path.append(root.val)
            sum = sum - root.val
            if root.left == None and root.right == None:
                if sum == 0:
                    paths.append(path)
            else:
                self.path(root.left, sum, paths, path[:])
                self.path(root.right, sum, paths, path[:])
            
                
