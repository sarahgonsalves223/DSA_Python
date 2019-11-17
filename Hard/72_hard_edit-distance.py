#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (38.96%)
# Total Accepted:    207.7K
# Total Submissions: 516.9K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following 3 operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time Complexity = O(m*n)
        Space Complexity = O(n)
        """
        dp = [0]*(len(word2)+1)
        for i in range(len(word1)+1):
            curr = [0]*(len(word2)+1)
            for j in range(len(word2)+1):
                if i == 0:
                    if j != 0:
                        curr[j] = curr[j-1] + 1
                elif j == 0:
                    curr[j] = dp[j] + 1
                else:
                    if word1[i-1] == word2[j-1]:
                        curr[j] = dp[j-1]
                    else:
                        curr[j] = min(dp[j-1], dp[j], curr[j-1]) + 1
            dp = curr
        return dp[-1]
