#
# @lc app=leetcode id=642 lang=python3
#
# [642] Design Search Autocomplete System
#
# https://leetcode.com/problems/design-search-autocomplete-system/description/
#
# algorithms
# Hard (39.07%)
# Total Accepted:    35.6K
# Total Submissions: 86.8K
# Testcase Example:  '["AutocompleteSystem","input","input","input","input"]\n[[["i love you","island","iroman","i love leetcode"],[5,3,2,2]],["i"],[" "],["a"],["#"]]'
#
# Design a search autocomplete system for a search engine. Users may input a
# sentence (at least one word and end with a special character '#'). For each
# character they type except '#', you need to return the top 3 historical hot
# sentences that have prefix the same as the part of sentence already typed.
# Here are the specific rules:
# 
# 
# The hot degree for a sentence is defined as the number of times a user typed
# the exactly same sentence before.
# The returned top 3 hot sentences should be sorted by hot degree (The first is
# the hottest one). If several sentences have the same degree of hot, you need
# to use ASCII-code order (smaller one appears first).
# If less than 3 hot sentences exist, then just return as many as you can.
# When the input is a special character, it means the sentence ends, and in
# this case, you need to return an empty list.
# 
# 
# Your job is to implement the following functions:
# 
# The constructor function:
# 
# AutocompleteSystem(String[] sentences, int[] times): This is the constructor.
# The input is historical data. Sentences is a string array consists of
# previously typed sentences. Times is the corresponding times a sentence has
# been typed. Your system should record these historical data.
# 
# Now, the user wants to input a new sentence. The following function will
# provide the next character the user types:
# 
# List<String> input(char c): The input c is the next character typed by the
# user. The character will only be lower-case letters ('a' to 'z'), blank space
# (' ') or a special character ('#'). Also, the previously typed sentence
# should be recorded in your system. The output will be the top 3 historical
# hot sentences that have prefix the same as the part of sentence already
# typed.
# 
# 
# Example:
# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love
# leetcode"], [5,3,2,2])
# The system have already tracked down the following sentences and their
# corresponding times:
# "i love you" : 5 times
# "island" : 3 times
# "ironman" : 2 times
# "i love leetcode" : 2 times
# Now, the user begins another search:
# 
# Operation: input('i')
# Output: ["i love you", "island","i love leetcode"]
# Explanation:
# There are four sentences that have prefix "i". Among them, "ironman" and "i
# love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has
# ASCII code 114, "i love leetcode" should be in front of "ironman". Also we
# only need to output top 3 hot sentences, so "ironman" will be ignored.
# 
# Operation: input(' ')
# Output: ["i love you","i love leetcode"]
# Explanation:
# There are only two sentences that have prefix "i ".
# 
# Operation: input('a')
# Output: []
# Explanation:
# There are no sentences that have prefix "i a".
# 
# Operation: input('#')
# Output: []
# Explanation:
# The user finished the input, the sentence "i a" should be saved as a
# historical sentence in system. And the following input will be counted as a
# new search.
# 
# 
# Note:
# 
# 
# The input sentence will always start with a letter and end with '#', and only
# one blank space will exist between two words.
# The number of complete sentences that to be searched won't exceed 100. The
# length of each sentence including those in the historical data won't exceed
# 100.
# Please use double-quote instead of single-quote when you write test cases
# even for a character input.
# Please remember to RESET your class variables declared in class
# AutocompleteSystem, as static/class variables are persisted across multiple
# test cases. Please see here for more details.
# 
# 
# 
# 
#
from collections import defaultdict
class TrieNode:
    def __init__(self, letter = "", endsHere = False):
        self.letter = letter
        self.endsHere = endsHere
        self.nodes = {}
        self.times = 0

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word, times):
        start = self.trie
        for ch in word:
            if ch not in start.nodes:
                node = TrieNode(ch)
                start.nodes[ch] = node
            start = start.nodes[ch]
        start.endsHere = True
        start.times = times

    def findWithPrefix(self, word):
        start = self.trie
        for ch in word:
            if ch in start.nodes:
                start = start.nodes[ch]
            else:
                return []
        ans = []
        curr = ""
        self.createWord(start, ans, curr, word)
        ans = sorted(ans, key=lambda element: (-element[0], element[1]))
        return ans

    def createWord(self, node, ans, curr, word):
        if node.endsHere:
            ans.append((node.times, word + curr))
        for ch in node.nodes:
            self.createWord(node.nodes[ch], ans, curr + ch, word)
        return ans
    
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.history = defaultdict(lambda:0)
        self.trie = Trie()
        self.word = ""
        for sentence, time in zip(sentences, times):
            self.history[sentence] = self.history[sentence] + time
            self.trie.addWord(sentence, time)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.history[self.word] = self.history[self.word] + 1
            self.trie.addWord(self.word, self.history[self.word])
            self.word = ""
            return []
        self.word = self.word + c
        ans = self.trie.findWithPrefix(self.word)
        ans = [an[1] for an in ans[:3]]
        return ans


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
