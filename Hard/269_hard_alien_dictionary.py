#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#
# https://leetcode.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (31.85%)
# Total Accepted:    100.9K
# Total Submissions: 305.6K
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# There is a new alien language which uses the latin alphabet. However, the
# order among letters are unknown to you. You receive a list of non-empty words
# from the dictionary, where words are sorted lexicographically by the rules of
# this new language. Derive the order of letters in this language.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠ "wrt",
# ⁠ "wrf",
# ⁠ "er",
# ⁠ "ett",
# ⁠ "rftt"
# ]
# 
# Output: "wertf"
# 
# 
# Example 2:
# 
# 
# Input:
# [
# ⁠ "z",
# ⁠ "x"
# ]
# 
# Output: "zx"
# 
# 
# Example 3:
# 
# 
# Input:
# [
# ⁠ "z",
# ⁠ "x",
# ⁠ "z"
# ] 
# 
# Output: "" 
# 
# Explanation: The order is invalid, so return "".
# 
# 
# Note:
# 
# 
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the
# given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is
# fine.
# 
# 
#
from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Time Complexity = O(n*m + w) where n is the num of words and m is the avg len of words and w is the total num of letters (might be constant)
        Space Complexity = O(w) -> most of the data structures store letters which are w (or 26)
        """
        outgoing = defaultdict(set)
        incoming = defaultdict(set)
        letters = set()
        for i in range(len(words)):
            for w in words[i]:
                letters.add(w)
        print(letters)
        for i in range(1, len(words)):
            ans = self.compare(words[i-1], words[i])
            if ans:
                outgoing[ans[0]].add(ans[1])
                incoming[ans[1]].add(ans[0])
        queue = deque([])
        for key in letters:
            if key not in incoming:
                queue.append(key)
        final_str = ""
        while queue:
            let = queue.popleft()
            final_str += let
            out = outgoing[let]
            for o in out:
                incoming[o].remove(let)
                if len(incoming[o]) == 0:
                    del incoming[o]
                    queue.append(o)
        if len(incoming) > 0:
            return ""
        return final_str
            
    def compare(self, one, two):
        i = 0
        j = 0
        
        while i < len(one) and j < len(two):
            if one[i] == two[j]:
                i += 1
                j += 1
                continue
            else:
                return (one[i], two[j])
        return None
        
            
