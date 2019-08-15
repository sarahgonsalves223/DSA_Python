"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_to_location = {}
        start, end, max_len = 0, 0, 0
        for i,c in enumerate(s):
            if c in char_to_location and char_to_location[c] >= start and char_to_location[c] <= end:
                start = 1 + char_to_location[c]
                end = i
                char_to_location[c] = i
            else:
                char_to_location[c] = i
                end = i
            length = end - start + 1
            max_len = max(length, max_len)
        return max_len
