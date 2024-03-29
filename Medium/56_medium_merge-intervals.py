#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (36.31%)
# Total Accepted:    385.9K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        pq = [(s,e) for s,e in intervals]
        heapq.heapify(pq)
        merged_intervals = []
        start = -1
        end = -1
        while pq:
            curr = heapq.heappop(pq)
            if end < curr[0]:
                merged_intervals.append([start, end])
                start = curr[0]
                end = curr[1]
            else:
                end = max(curr[1], end)
        
        merged_intervals.append([start, end])
        return merged_intervals[1:]
            
