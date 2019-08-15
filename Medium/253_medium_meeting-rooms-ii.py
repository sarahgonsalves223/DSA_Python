#
# @lc app=leetcode id=253 lang=python
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (43.33%)
# Total Accepted:    170.7K
# Total Submissions: 394K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
# 
# Example 1:
# 
# 
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 
# Example 2:
# 
# 
# Input: [[7,10],[2,4]]
# Output: 1
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start_pq = [(x,y) for x,y in intervals]
        heapq.heapify(start_pq)
        
        end_pq = []

        curr = 0
        while start_pq:
            interval = heapq.heappop(start_pq)
            while end_pq and end_pq[0][0] <= interval[0]:
                heapq.heappop(end_pq)
            heapq.heappush(end_pq, (interval[1],interval[0]))
            curr = max(curr, len(end_pq))
        
        return curr
                
