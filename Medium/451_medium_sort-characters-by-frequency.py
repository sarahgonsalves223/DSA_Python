#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (56.94%)
# Total Accepted:    112.4K
# Total Submissions: 195.1K
# Testcase Example:  '"tree"'
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.
# 
# Example 1:
# 
# Input:
# "tree"
# 
# Output:
# "eert"
# 
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
# 
# 
# 
# Example 2:
# 
# Input:
# "cccaaa"
# 
# Output:
# "cccaaa"
# 
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# 
# 
# 
# Example 3:
# 
# Input:
# "Aabb"
# 
# Output:
# "bbAa"
# 
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
# 
# 
#
from collections import Counter
import operator
class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Used a counter to count the occurences and then sort the dict by value
        n = len(s) 
        Space Complexity = O(n)
        Time Complexity = O(nlogn + n)
        """
        count = Counter(s)
        
        count = sorted(count.items(), key=operator.itemgetter(1),reverse=True)
        ans = ""
        for key in count:
            ans += key[0]*key[1]
        
        return ans
