#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (58.35%)
# Total Accepted:    69.2K
# Total Submissions: 118.6K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# You need to find the largest value in each row of a binary tree.
# 
# Example:
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# Output: [1, 3, 9]
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        q = deque()
        q.append(root)
        while len(q) > 0:
            maxi = -float("Inf")
            qu = deque()
            while len(q) > 0:
                node = q.popleft()
                if node.val > maxi:
                    maxi = node.val
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            ans.append(maxi)
            q = deque(qu)
        
        return ans
            
