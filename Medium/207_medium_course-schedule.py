#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (38.80%)
# Total Accepted:    242.3K
# Total Submissions: 624.4K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
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
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        incoming = {}
        outgoing = {}
        
        for prereq in prerequisites:
            one = prereq[0]
            two = prereq[1]
            if one not in incoming:
                incoming[one] = [two]
            else:
                incoming[one].append(two)
            if two not in outgoing:
                outgoing[two] = [one]
            else:
                outgoing[two].append(one)
                
        queue = deque([])
        for i in range(numCourses):
            if i not in incoming:
                queue.append(i)
        
        while len(queue) > 0:
            course = queue.popleft()
            if course in outgoing:
                courses = outgoing[course]
                for out in courses:
                    if out in incoming:
                        incoming[out].remove(course)
                        if len(incoming[out]) == 0:
                            incoming.pop(out, None)
                            queue.append(out)
        return len(incoming) == 0
                    
                
        print(outgoing)
        print(incoming)
        return False
