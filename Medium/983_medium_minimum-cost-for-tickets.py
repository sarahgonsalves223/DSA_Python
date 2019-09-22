#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#
# https://leetcode.com/problems/minimum-cost-for-tickets/description/
#
# algorithms
# Medium (57.55%)
# Total Accepted:    21.9K
# Total Submissions: 37.9K
# Testcase Example:  '[1,4,6,7,8,20]\n[2,7,15]'
#
# In a country popular for train travel, you have planned some train travelling
# one year in advance.  The days of the year that you will travel is given as
# an array days.  Each day is an integer from 1 to 365.
# 
# Train tickets are sold in 3 different ways:
# 
# 
# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# 
# 
# The passes allow that many days of consecutive travel.  For example, if we
# get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6,
# 7, and 8.
# 
# Return the minimum number of dollars you need to travel every day in the
# given list of days.
# 
# 
# 
# Example 1:
# 
# 
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel
# plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4,
# ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.
# 
# 
# 
# Example 2:
# 
# 
# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel
# plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1,
# 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total you spent $17 and covered all the days of your travel.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000
# 
# 
#
import bisect
class Solution:
    def __init__(self):
        self.cache = {}
        
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Space Complexity = O(n)
        Time Complexity = O(n*log(n))
        """
        return self.helper(days, costs)
    
    def helper(self, days, costs):
        tp = tuple(days)
        if tp in self.cache:
            return self.cache[tp]
        if len(days) < 2:
            return len(days)*min(costs)
        
        index = bisect.bisect_left(days, days[0] + 1)
        daily = costs[0] + self.helper(days[index:], costs)
        index = bisect.bisect_left(days, days[0] + 7)
        weekly = costs[1] + self.helper(days[index:], costs)
        index = bisect.bisect_left(days, days[0] + 30)
        monthly = costs[2] + self.helper(days[index:], costs)
        mini = min(daily, weekly, monthly)
        self.cache[tp] = mini
        return mini
            
            
            
        
