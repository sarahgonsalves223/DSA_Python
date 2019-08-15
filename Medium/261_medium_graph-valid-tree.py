#
# @lc app=leetcode id=261 lang=python
#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (40.27%)
# Total Accepted:    94.7K
# Total Submissions: 235.2K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
# is a pair of nodes), write a function to check whether these edges make up a
# valid tree.
# 
# Example 1:
# 
# 
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# 
# Example 2:
# 
# 
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# 
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0,1] is the same as [1,0] and thus will not appear
# together in edges.
# 
#
class Solution(object):
    
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) >= n or len(edges) < n-1:
            return False
        
        self.parents = range(n)
        for edge in edges:
            if self.find(edge[0]) == self.find(edge[1]):
                return False
            self.union(edge[0], edge[1])
        return True

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        self.parents[i] = j
    
    def find(self, i):
        while self.parents[i] != i:
            i = self.parents[i]
        return i
    
    
