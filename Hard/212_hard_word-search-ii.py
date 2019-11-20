#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (29.64%)
# Total Accepted:    145.3K
# Total Submissions: 469.2K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]'
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
# 
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
# 
# 
# 
# Example:
# 
# 
# Input: 
# board = [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
# 
# Output: ["eat","oath"]
# 
# 
# 
# 
# Note:
# 
# 
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
# 
# 
#
class TrieNode:
    def __init__(self, letter = "", endsHere = False):
        self.letter = letter
        self.endsHere = endsHere
        self.nodes = {}
        
class Trie:
    def __init__(self):
        self.trie = TrieNode()
    
    def addWord(self, word):
        start = self.trie
        for ch in word:
            if ch in start.nodes:
                start = start.nodes[ch]
            else:
                node = TrieNode(ch)
                start.nodes[ch] = node
                start = start.nodes[ch]
        start.endsHere = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Time Complexity = God only knows!!
        Space Complexity = O(N)
        """
        trie = Trie()
        for word in words:
            trie.addWord(word)
        ans = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.findWord(board, i, j, set(), trie.trie, ans, [])
        return list(ans)
    
    def findWord(self, board, i, j, used, trie, ans, word):
        if trie.endsHere:
            ans.add("".join(word))
        if i >= len(board) or i < 0 or j < 0 or j >= len(board[0]):
            return
        elif (i,j) in used or board[i][j] not in trie.nodes:
            return
        ch = board[i][j]
        trie = trie.nodes[ch]
        word.append(ch)
        used.add((i,j))
        self.findWord(board, i+1, j, used, trie, ans, word)
        self.findWord(board, i, j+1, used, trie, ans, word)
        self.findWord(board, i-1, j, used, trie, ans, word)
        self.findWord(board, i, j-1, used, trie, ans, word)
        used.remove((i,j))
        word.pop()
            
    
    
