#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (60.43%)
# Total Accepted:    81.6K
# Total Submissions: 135K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# 
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# 
#
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        temps = {}
        days = [0]*len(T)
        for i,t in enumerate(T):
            for temp in temps.items():
                temp = temp[0]
                if temp < t:
                    locs = temps[temp]
                    for loc in locs:
                        days[loc] = i - loc
                    del temps[temp]
            if t in temps:
                temps[t].append(i)
            else:
                temps[t] = [i]
        return days
