#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (32.07%)
# Total Accepted:    314K
# Total Submissions: 978.9K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0]*len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited = [[0]*len(board[0]) for i in range(len(board))]
                    if self.find(visited, board, word, 0, i, j):
                        return True
        return False
            
    def find(self, visited, board, word, index, row, col):
        if index >= len(word) or board[row][col] != word[index] or visited[row][col]:
            return False
        if index == len(word) - 1:
            return True
        visited[row][col] = 1
        if row-1 >= 0 and visited[row-1][col] == 0:
            if self.find(visited, board, word, index+1, row-1, col):
                return True
            visited[row-1][col] = 0
        if row+1 < len(board) and visited[row+1][col] == 0:
            if self.find(visited, board, word, index+1, row+1, col):
                return True
            visited[row+1][col] = 0
        if col-1 >= 0 and visited[row][col-1] == 0:
            if self.find(visited, board, word, index+1, row, col-1):
                return True
            visited[row][col-1] = 0
        if col+1 < len(board[0]) and visited[row][col+1] == 0:
            if self.find(visited, board, word, index+1, row, col+1):
                return True
            visited[row][col+1] = 0
        return False
        
