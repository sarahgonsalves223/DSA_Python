#
# @lc app=leetcode id=366 lang=python3
#
# [366] Find Leaves of Binary Tree
#
# https://leetcode.com/problems/find-leaves-of-binary-tree/description/
#
# algorithms
# Medium (66.76%)
# Total Accepted:    48.9K
# Total Submissions: 73.2K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a binary tree, collect a tree's nodes as if you were doing this:
# Collect and remove all leaves, repeat until the tree is empty.
# 
# 
# 
# Example:
# 
# 
# Input: [1,2,3,4,5]
# 
# 1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# Output: [[4,5,3],[2],[1]]
# 
# 
# 
# 
# Explanation:
# 
# 1. Removing the leaves [4,5,3] would result in this tree:
# 
# 
# ⁠         1
# ⁠        / 
# ⁠       2          
# 
# 
# 
# 
# 2. Now removing the leaf [2] would result in this tree:
# 
# 
# ⁠         1          
# 
# 
# 
# 
# 3. Now removing the leaf [1] would result in the empty tree:
# 
# 
# ⁠         []         
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.listie = []
        self.findDepth(root, self.listie)
        return self.listie
    
    def findDepth(self, root: TreeNode, listie: List[List[int]]) -> int:
        if not root:
            depth = 0
            return depth
        elif root.left == None and root.right == None:
            depth = 1
        else:
            depth = 1 + max(self.findDepth(root.left, listie), self.findDepth(root.right, listie))
        
        if len(listie) >= depth:
            listie[depth-1].append(root.val)
        else:
            listie.append([root.val])
        
        return depth
        
