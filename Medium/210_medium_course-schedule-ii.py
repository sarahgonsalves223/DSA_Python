#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (35.82%)
# Total Accepted:    164.1K
# Total Submissions: 458.2K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
from collections import defaultdict, deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        incoming = [0]*numCourses
        outgoing = defaultdict(list)
        queue = deque([])
        for prereqs in prerequisites:
            s = prereqs[0]
            e = prereqs[1]
            incoming[s] += 1
            outgoing[e].append(s)
            
        for i,course in enumerate(incoming):
            if course == 0:
                queue.append(i)
        
        schedule = []
        while len(queue) > 0:
            course = queue.popleft()
            schedule.append(course)
            for out in outgoing[course]:
                incoming[out] -= 1
                if incoming[out] == 0:
                    queue.append(out)
        
        if len(schedule) < numCourses:
            return []
        else:
            return schedule
            
            
        
