#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (42.50%)
# Total Accepted:    402.4K
# Total Submissions: 947K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    grid = self.makeZero(grid, i, j)
        return count
    
    def makeZero(self, grid: List[List[str]], row: int, col: int) -> List[List[str]]:
        if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
            return
        if grid[row][col] == "0":
            return
        grid[row][col] = "0"
        #right
        self.makeZero(grid, row, col+1)
        #left
        self.makeZero(grid, row, col-1)
        #down
        self.makeZero(grid, row+1, col)
        #up
        self.makeZero(grid, row-1, col)
        return grid
