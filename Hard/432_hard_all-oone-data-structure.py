#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#
# https://leetcode.com/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (30.21%)
# Total Accepted:    23.7K
# Total Submissions: 76.7K
# Testcase Example:  '["AllOne","getMaxKey","getMinKey"]\n[[],[],[]]'
#
# Implement a data structure supporting the following operations:
# 
# 
# 
# Inc(Key) - Inserts a new key  with value 1. Or increments an existing key by
# 1. Key is guaranteed to be a non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise
# decrements an existing key by 1. If the key does not exist, this function
# does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element
# exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element
# exists, return an empty string "".
# 
# 
# 
# 
# Challenge: Perform all these in O(1) time complexity.
# 
#
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.keys:
            self.keys[key] = self.keys[key] + 1
        else:
            self.keys[key] = 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.keys:
            if self.keys[key] == 1:
                del self.keys[key]
            else:
                self.keys[key] = self.keys[key] - 1
            
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        maxk = 0
        value = ""
        for key in self.keys:
            if self.keys[key] > maxk:
                maxk = self.keys[key]
                value = key
        return value

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        mink = float('inf')
        value = ""
        for key in self.keys:
            if self.keys[key] < mink:
                mink = self.keys[key]
                value = key
        return value
                   
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
