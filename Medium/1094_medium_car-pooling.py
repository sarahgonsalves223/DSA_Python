#
# @lc app=leetcode id=1094 lang=python
#
# [1094] Car Pooling
#
# https://leetcode.com/problems/car-pooling/description/
#
# algorithms
# Medium (57.55%)
# Total Accepted:    8.4K
# Total Submissions: 14.6K
# Testcase Example:  '[[2,1,5],[3,3,7]]\n4'
#
# You are driving a vehicle that has capacity empty seats initially available
# for passengers.  The vehicle only drives east (ie. it cannot turn around and
# drive west.)
# 
# Given a list of trips, trip[i] = [num_passengers, start_location,
# end_location] contains information about the i-th trip: the number of
# passengers that must be picked up, and the locations to pick them up and drop
# them off.  The locations are given as the number of kilometers due east from
# your vehicle's initial location.
# 
# Return true if and only if it is possible to pick up and drop off all
# passengers for all the given trips. 
# 
# 
# 
# Example 1:
# 
# 
# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: trips = [[2,1,5],[3,5,7]], capacity = 3
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
# Output: true
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# trips.length <= 1000
# trips[i].length == 3
# 1 <= trips[i][0] <= 100
# 0 <= trips[i][1] < trips[i][2] <= 1000
# 1 <= capacity <= 100000
# 
#
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        start_pq = [(y,z,x) for x,y,z in trips]
        heapq.heapify(start_pq)
        end_pq = []
        while start_pq:
            trip = heapq.heappop(start_pq)
            while end_pq and end_pq[0][0] <= trip[0]:
                prev = heapq.heappop(end_pq)
                capacity += prev[2]
            
            heapq.heappush(end_pq, (trip[1], trip[0], trip[2]))
            capacity -= trip[2]
            if capacity < 0:
                return False
        
        return True
                
    
