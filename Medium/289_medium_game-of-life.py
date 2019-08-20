#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (47.09%)
# Total Accepted:    124.7K
# Total Submissions: 264.9K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
# 
# Example:
# 
# 
# Input: 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# Output: 
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
# 
# 
#
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                alive = 0
                #up
                if i-1 >=0 and board[i-1][j]>0:
                    alive += 1
                #down
                if i+1 < len(board) and board[i+1][j]>0:
                    alive += 1
                #left
                if j-1 >= 0 and board[i][j-1] > 0:
                    alive += 1
                #right
                if j+1 < len(board[0]) and board[i][j+1]>0:
                    alive += 1
                #topleft
                if i-1 >=0 and j-1 >= 0 and board[i-1][j-1]>0:
                    alive += 1
                #topright
                if i-1 >=0 and j+1 < len(board[0]) and board[i-1][j+1]>0:
                    alive += 1
                #bottomleft
                if i+1 < len(board) and j-1 >= 0 and board[i+1][j-1]>0:
                    alive += 1
                #bottomright
                if i+1 < len(board) and j+1 < len(board[0]) and board[i+1][j+1]>0:
                    alive += 1
                if board[i][j]:
                    if alive < 2 or alive > 3:
                        board[i][j] = 2
                else:
                    if alive == 3:
                        board[i][j] = -1
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0 or board[i][j] == 2:
                    board[i][j] = 0
                else:
                    board[i][j] = 1
        return board
