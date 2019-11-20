#
# @lc app=leetcode id=272 lang=python3
#
# [272] Closest Binary Search Tree Value II
#
# https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/
#
# algorithms
# Hard (46.13%)
# Total Accepted:    45.7K
# Total Submissions: 96.1K
# Testcase Example:  '[4,2,5,1,3]\n3.714286\n2'
#
# Given a non-empty binary search tree and a target value, find k values in the
# BST that are closest to the target.
# 
# Note:
# 
# 
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that
# are closest to the target.
# 
# 
# Example:
# 
# 
# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
# 
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
# 
# Output: [4,3]
# 
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime
# (where n = total nodes)?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        """
        Time Complexity = O(nlogk)
        Space Complexity = O(k)
        """
        heap = []
        heapq.heapify(heap)
        self.findKClosest(root, target, k, heap)
        ans = []
        return [val[1] for val in heap]
    
    def findKClosest(self, root, target, k, heap):
        
        if not root:
            return
        diff = abs(root.val - target)
        if len(heap) < k:
            heapq.heappush(heap, (-diff, root.val))
        else:
            if -1*heap[0][0] > diff:
                heapq.heappop(heap)
                heapq.heappush(heap, (-diff, root.val))
        self.findKClosest(root.left, target, k, heap)
        self.findKClosest(root.right, target, k, heap)
                
    
        
