#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (49.19%)
# Total Accepted:    228.2K
# Total Submissions: 457.6K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = self.helper(1, n, k)
        return ans
        
    def helper(self, start, n, k):
        if start > n or k==0:
            return []
        if k == 1:
            return [[i] for i in range(start, n+1)]
        ans = []
        for i in range(start, n+1):
            lists = self.helper(i+1, n, k-1)
            for list1 in lists:
                list1 = [i] + list1
                ans.append(list1)
        return ans
