#
# @lc app=leetcode id=252 lang=python
#
# [252] Meeting Rooms
#
# https://leetcode.com/problems/meeting-rooms/description/
#
# algorithms
# Easy (52.53%)
# Total Accepted:    91.7K
# Total Submissions: 174.6K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
# meetings.
# 
# Example 1:
# 
# 
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# 
# 
# Example 2:
# 
# 
# Input: [[7,10],[2,4]]
# Output: true
# 
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
#import heapq
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        pq = [(x,y) for x,y in intervals]
        heapq.heapify(pq)
        prev = heapq.heappop(pq)
        while pq:
            node = heapq.heappop(pq)
            if prev[1]>node[0]:
                return False
            prev = node
        return True
        
