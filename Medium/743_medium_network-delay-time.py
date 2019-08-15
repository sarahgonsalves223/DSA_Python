#
# @lc app=leetcode id=743 lang=python
#
# [743] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Medium (43.28%)
# Total Accepted:    41.1K
# Total Submissions: 95K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# There are N network nodes, labelled 1 to N.
# 
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
# 
# Now, we send a signal from a certain node K. How long will it take for all
# nodes to receive the signal? If it is impossible, return -1.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
# 
# 
#
from collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        pq = [(0,K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for neig, d2 in graph[node]:
                if neig not in dist:
                    heapq.heappush(pq, (d+d2, neig))
        return max(dist.values()) if len(dist) == N else -1
                
        
        
        
