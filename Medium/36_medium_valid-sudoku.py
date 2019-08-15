#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (44.16%)
# Total Accepted:    256.6K
# Total Submissions: 581.2K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
# 
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without
# repetition.
# 
# 
# 
# A partially filled sudoku which is valid.
# 
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠ ["5","3",".",".","7",".",".",".","."],
# ⁠ ["6",".",".","1","9","5",".",".","."],
# ⁠ [".","9","8",".",".",".",".","6","."],
# ⁠ ["8",".",".",".","6",".",".",".","3"],
# ⁠ ["4",".",".","8",".","3",".",".","1"],
# ⁠ ["7",".",".",".","2",".",".",".","6"],
# ⁠ [".","6",".",".",".",".","2","8","."],
# ⁠ [".",".",".","4","1","9",".",".","5"],
# ⁠ [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# [
# ["8","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being 
# ⁠   modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is
# invalid.
# 
# 
# Note:
# 
# 
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.
# 
# 
#
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {}
        cols = {}
        blocks = {}
        for i,row in enumerate(board):
            for j,val in enumerate(row):
                if val == ".":
                    continue
                if i in rows:
                    if val in rows[i]:
                        return False
                    else:
                        rows[i].add(val)
                else:
                    rows[i] = set()
                    rows[i].add(val)
                
                if j in cols:
                    if val in cols[j]:
                        return False
                    else:
                        cols[j].add(val)
                else:
                    cols[j] = set()
                    cols[j].add(val)
                
                block = self.getBlock(i, j)
                if block in blocks:
                    if val in blocks[block]:
                        return False
                    else:
                        blocks[block].add(val)
                else:
                    blocks[block] = set()
                    blocks[block].add(val)
        return True
    
    def getBlock(self, i, j):
        if i >= 0 and i <=2:
            if j >=0 and j<=2:
                return 0
            if j>=3 and j<=5:
                return 1
            else:
                return 2
        elif i>=3 and i<=5:
            if j >=0 and j<=2:
                return 3
            if j>=3 and j<=5:
                return 4
            else:
                return 5
        else:
            if j >=0 and j<=2:
                return 6
            if j>=3 and j<=5:
                return 7
            else:
                return 8
