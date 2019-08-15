#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#
# https://leetcode.com/problems/two-sum-iii-data-structure-design/description/
#
# algorithms
# Easy (31.12%)
# Total Accepted:    62.4K
# Total Submissions: 200.5K
# Testcase Example:  '["TwoSum","add","add","add","find","find"]\n[[],[1],[3],[5],[4],[7]]'
#
# Design and implement a TwoSum class. It should support the following
# operations: add and find.
# 
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the
# value.
# 
# Example 1:
# 
# 
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# 
# 
# Example 2:
# 
# 
# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false
# 
#
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.map:
            self.map[number] = 1
        else:
            self.map[number] = self.map[number] + 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        
        for key in self.map.keys():
            remain = value - key
            if remain != key and remain in self.map:
                return True
            elif remain == key and self.map[remain] > 1:
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
