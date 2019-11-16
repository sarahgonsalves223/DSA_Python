#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (16.00%)
# Total Accepted:    134.7K
# Total Submissions: 827.9K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
# 
# Example 1:
# 
# 
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# 
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Time Complexity = O(n^2)
        Space Complexity = O(n-1)
        """
        
        if len(points) == 0:
            return 0
        if len(points) < 3:
            return len(points)
        max_count = 1
        for i in range(len(points)-1):
            count = 1
            lines = defaultdict(lambda:0)
            horizontal = 0
            duplicates = 0
            for j in range(i+1, len(points)):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                elif y1 == y2:
                    horizontal += 1
                    count = max(count, horizontal+1)
                else:
                    slope = (x1-x2)/(y1-y2)
                    lines[slope] = lines[slope] + 1
                    count = max(count, lines[slope]+1)
            max_count = max(max_count, count+duplicates)
        return max_count
                
    
