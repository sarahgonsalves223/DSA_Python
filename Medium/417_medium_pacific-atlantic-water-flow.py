#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (38.14%)
# Total Accepted:    54K
# Total Submissions: 139.9K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# 
# 
# Example:
# 
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
# 
# 
#
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity = O(m*n)
        Space Complexity = O(m*n)
        """
        pacific = set()
        atlantic = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    self.visitOcean(matrix, pacific, (i,j))
                if i == len(matrix)-1 or j == len(matrix[0])-1:
                    self.visitOcean(matrix, atlantic, (i,j))
        return list(pacific.intersection(atlantic))
        
    
    def visitOcean(self, matrix, ocean, point):
        if point in ocean:
            return
        else:
            ocean.add(point)
            i = point[0]
            j = point[1]
            #up
            if i > 0 and matrix[i][j] <= matrix[i-1][j]:
                self.visitOcean(matrix, ocean, (i-1,j))
            #down
            if i < len(matrix)-1 and matrix[i][j] <= matrix[i+1][j]:
                 self.visitOcean(matrix, ocean, (i+1,j))
            #left
            if j > 0 and matrix[i][j] <= matrix[i][j-1]:
                self.visitOcean(matrix, ocean, (i,j-1))
            #right
            if j < len(matrix[0])-1 and matrix[i][j] <= matrix[i][j+1]:
                self.visitOcean(matrix, ocean, (i,j+1))
                
        
        
