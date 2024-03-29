#
# @lc app=leetcode id=399 lang=python
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (48.29%)
# Total Accepted:    88.4K
# Total Submissions: 183K
# Testcase Example:  '[["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# Equations are given in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given  a / b = 2.0, b / c = 3.0.
# queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
# 
# According to the example above:
# 
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]
# ]. 
# 
# 
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
#
from collections import defaultdict, deque
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)
        
        def build_graph(equations, values):
            def add_edge(s, e, value):
                graph[s].append((e,value))
            
            for eq, value in zip(equations, values):
                add_edge(eq[0], eq[1], value)
                add_edge(eq[1], eq[0], 1/value)
            
        def find_path(s, e):
            if s not in graph or e not in graph:
                return -1.0
            
            visited = set()
            queue = deque([(s, 1.0)])
            while queue:
                curr, prod = queue.popleft()
                visited.add(curr)
                if e == curr:
                    return prod
                for neighbor in graph[curr]:
                    if neighbor[0] not in visited:
                        queue.append((neighbor[0], prod*neighbor[1]))
            return -1.0
        
        build_graph(equations, values)
        ans = []
        for q in queries:
            ans.append(find_path(q[0],q[1]))
        return ans
        
