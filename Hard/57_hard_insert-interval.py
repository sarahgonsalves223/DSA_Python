#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (31.62%)
# Total Accepted:    203.3K
# Total Submissions: 634.6K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time complexity = O(n) since the input intervals are already sorted
        Space Complexity = O(n) to store the output
        """
        if not intervals or len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        final_intervals = []
        for i, interval in enumerate(intervals):
            if self.overlapping(newInterval, interval):
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
                if i == len(intervals) - 1:
                    final_intervals.append(newInterval)
            else:
                if newInterval[1] < interval[0]:
                    final_intervals.append(newInterval)
                    final_intervals.extend(intervals[i:])
                    break
                else:
                    final_intervals.append(interval)
                    if i == len(intervals) - 1:
                        final_intervals.append(newInterval)
        
        return final_intervals
    
    def overlapping(self, one, two):
        ints = sorted([one,two])
        one = ints[0]
        two = ints[1]
        if two[0] <= one[1]:
            return True
        return False

        
                
