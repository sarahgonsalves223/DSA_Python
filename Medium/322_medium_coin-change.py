#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (31.45%)
# Total Accepted:    264.3K
# Total Submissions: 816.9K
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# Example 1:
# 
# 
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
#
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Time Complexity = O(amount*len(coins))
        Space Complexity = O(amount*len(coins))
        """
        matrix = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    if j != 0:
                        matrix[i][j] = float('inf')
                elif j == 0:
                    matrix[i][j] = 0
                else:
                    if coins[i-1] <= j:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-coins[i-1]]+1)
                    else:
                        matrix[i][j] = matrix[i-1][j]
        if matrix[len(matrix)-1][len(matrix[0])-1] < float('inf'):
            return matrix[len(matrix)-1][len(matrix[0])-1]
        else:
            return -1
