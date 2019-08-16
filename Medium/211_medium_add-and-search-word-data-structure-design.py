#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (31.33%)
# Total Accepted:    123.9K
# Total Submissions: 395.6K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#
class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.endsHere = False
        self.nodes = {}
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode("")

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.trie
        for w in word:
            if w in curr.nodes:
                curr = curr.nodes[w]
            else:
                curr.nodes[w] = TrieNode(w)
                curr = curr.nodes[w]
        curr.endsHere = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self.trie
        return self.searchInNode(word, curr)
    
    def searchInNode(self, word, curr) -> bool:
        for i,w in enumerate(word):
            if w == ".":
                for node in curr.nodes:
                    if self.searchInNode(word[i+1:], curr.nodes[node]):
                        return True
                return False
            elif w in curr.nodes:
                curr = curr.nodes[w]
            else:
                return False
        return curr.endsHere
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
