#
# @lc app=leetcode id=1065 lang=python3
#
# [1065] Index Pairs of a String
#
# https://leetcode.com/problems/index-pairs-of-a-string/description/
#
# algorithms
# Easy (57.37%)
# Total Accepted:    2.5K
# Total Submissions: 4.4K
# Testcase Example:  '"thestoryofleetcodeandme"\n["story","fleet","leetcode"]'
#
# Given a text string and words (a list of strings), return all index pairs [i,
# j] so that the substring text[i]...text[j] is in the list of words.
# 
# 
# 
# Example 1:
# 
# 
# Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
# Output: [[3,7],[9,13],[10,17]]
# 
# 
# Example 2:
# 
# 
# Input: text = "ababa", words = ["aba","ab"]
# Output: [[0,1],[0,2],[2,3],[2,4]]
# Explanation: 
# Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].
# 
# 
# 
# 
# Note:
# 
# 
# All strings contains only lowercase English letters.
# It's guaranteed that all strings in words are different.
# 1 <= text.length <= 100
# 1 <= words.length <= 20
# 1 <= words[i].length <= 50
# Return the pairs [i,j] in sorted order (i.e. sort them by their first
# coordinate in case of ties sort them by their second coordinate).
# 
#
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        for word in words:
            ans2 = self.findOccur(text, word)
            if len(ans2) > 0:
                ans.extend(ans2)
        return sorted(ans)
    
    def findOccur(self, word: str, sub: str) -> List[int]:
        ans = []
        for i in range(0, len(word) - len(sub) + 1):
            if word[i:len(sub)+i] == sub:
                ans.append([i, len(sub)+i-1])
        return ans
