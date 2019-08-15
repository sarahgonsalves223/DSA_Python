#
# @lc app=leetcode id=243 lang=python
#
# [243] Shortest Word Distance
#
# https://leetcode.com/problems/shortest-word-distance/description/
#
# algorithms
# Easy (58.07%)
# Total Accepted:    71.6K
# Total Submissions: 123.2K
# Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n"coding"\n"practice"'
#
# Given a list of words and two words word1 and word2, return the shortest
# distance between these two words in the list.
# 
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# 
# 
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# 
# 
# 
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# 
# 
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are
# both in the list.
# 
#
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        word1_ind = float('Inf')
        word2_ind = float('Inf')
        diff = float('Inf')
        for i,word in enumerate(words):
            if word == word1:
                word1_ind = i
            elif word == word2:
                word2_ind = i
            temp_diff = abs(word1_ind - word2_ind)
            if  temp_diff < diff:
                diff = temp_diff
        return diff
        
