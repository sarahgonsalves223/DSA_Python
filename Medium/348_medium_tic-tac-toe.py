#
# @lc app=leetcode id=348 lang=python3
#
# [348] Design Tic-Tac-Toe
#
# https://leetcode.com/problems/design-tic-tac-toe/description/
#
# algorithms
# Medium (50.49%)
# Total Accepted:    52.6K
# Total Submissions: 104.3K
# Testcase Example:  '["TicTacToe","move","move","move","move","move","move","move"]\n[[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]'
#
# Design a Tic-tac-toe game that is played between two players on a n x n
# grid.
# 
# 
# You may assume the following rules:
# 
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical,
# or diagonal row wins the game.
# 
# 
# 
# Example:
# 
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
# 
# TicTacToe toe = new TicTacToe(3);
# 
# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |
# 
# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |
# 
# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|
# 
# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|
# 
# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|
# 
# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|
# 
# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
# 
# 
# 
# Follow up:
# Could you do better than O(n2) per move() operation?
# 
#
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        inner_map_one = {"row" : [0]*n, "col": [0]*n, "diag": [0,0]}
        inner_map_two = {"row" : [0]*n, "col": [0]*n, "diag": [0,0]}
        self.status = {1: inner_map_one, 2: inner_map_two}

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        player_status = self.status[player]
        player_status["row"][row] += 1
        player_status["col"][col] += 1
        if row == col:
            player_status["diag"][0] += 1
        if row+col == self.n-1:
            player_status["diag"][1] += 1
        if player_status["row"][row] == self.n or player_status["col"][col] == self.n or player_status["diag"][0] == self.n or player_status["diag"][1] == self.n:
            return player
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
