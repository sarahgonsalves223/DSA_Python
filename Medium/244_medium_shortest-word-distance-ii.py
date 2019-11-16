#
# @lc app=leetcode id=244 lang=python3
#
# [244] Shortest Word Distance II
#
# https://leetcode.com/problems/shortest-word-distance-ii/description/
#
# algorithms
# Medium (48.55%)
# Total Accepted:    59.2K
# Total Submissions: 118.4K
# Testcase Example:  '["WordDistance","shortest","shortest"]\n[[["practice","makes","perfect","coding","makes"]],["coding","practice"],["makes","coding"]]'
#
# Design a class which receives a list of words in the constructor, and
# implements a method that takes two words word1 and word2 and return the
# shortest distance between these two words in the list. Your method will be
# called repeatedly many times with different parameters. 
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
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are
# both in the list.
# 
#
from collections import defaultdict
class WordDistance:

    def __init__(self, words: List[str]):
        self.positions = defaultdict(list)
        for i, word in enumerate(words):
            self.positions[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        pone = self.positions[word1]
        ptwo = self.positions[word2]
        one = 0 
        two = 0
        mini = float('inf')
        while one < len(pone) and two < len(ptwo):
            diff = abs(pone[one]-ptwo[two])
            mini = min(mini, diff)
            if pone[one] < ptwo[two]:
                one += 1
            else:
                two += 1
        return mini

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
