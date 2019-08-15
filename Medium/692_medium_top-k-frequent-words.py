#
# @lc app=leetcode id=692 lang=python
#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (46.61%)
# Total Accepted:    75.5K
# Total Submissions: 162.1K
# Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
#
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two
# words have the same frequency, then the word with the lower alphabetical
# order comes first.
# 
# Example 1:
# 
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# ⁠   Note that "i" comes before "love" due to a lower alphabetical order.
# 
# 
# 
# Example 2:
# 
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
# "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# ⁠   with the number of occurrence being 4, 3, 2 and 1 respectively.
# 
# 
# 
# Note:
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# 
# 
# 
# Follow up:
# 
# Try to solve it in O(n log k) time and O(n) extra space.
# 
# 
#
from collections import defaultdict, Counter
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = Counter(words)
        pq = []
        for word, count in counter.iteritems():
            heapq.heappush(pq, (-count, word))
        ans = []
        while k:
            ans.append(heapq.heappop(pq)[1])
            k -= 1
        return ans
        
        
