#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (39.86%)
# Total Accepted:    193.6K
# Total Submissions: 485.7K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#
class TrieNode:
    def __init__(self, letter):
        self.nodes = {}
        self.letter = letter
        self.endsHere = False
        
class Trie: 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.trie
        for let in word:
            if let in curr.nodes:
                  curr = curr.nodes[let]
            else:
                curr.nodes[let] = TrieNode(let)
                curr = curr.nodes[let]
        curr.endsHere = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.trie
        for let in word:
            if let in curr.nodes:
                curr = curr.nodes[let]
            else:
                return False
        return curr.endsHere

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.trie
        for let in prefix:
            if let in curr.nodes:
                curr = curr.nodes[let]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
