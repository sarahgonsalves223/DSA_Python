#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (38.01%)
# Total Accepted:    140.3K
# Total Submissions: 354.3K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
# 
# [2,3,4], the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# 
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
# 
# 
# 
# 
# Example:
# 
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 
# 
# 
# Follow up:
# 
# 
# If all integer numbers from the stream are between 0 and 100, how would you
# optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how
# would you optimize it?
# 
# 
#
import heapq
class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)

    def addNum(self, num: int) -> None:
        """
        Time Complexity = O(5*logn)
        5 for the 5 following steps:
        1. Adding element to heap (logn)
        2. If imbalanced, removing from the two heaps (2*logn)
        3. And adding back into the two heaps (2*logn)
        
        Space Complexity = O(n)
        """        
        if len(self.minheap) == len(self.maxheap):
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -1*num)
        
        if self.minheap and self.maxheap and self.minheap[0] < -1*self.maxheap[0]:
            right = heapq.heappop(self.minheap)
            left = -1*heapq.heappop(self.maxheap)
            heapq.heappush(self.maxheap, -1*right)
            heapq.heappush(self.minheap, left)

    def findMedian(self) -> float:
        """
        Time Complexity: O(1)
        Fetching the two top elements from both the heaps if length is equal, else fetching from the min heap which we assume is always larger.
        """
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + (-1 * self.maxheap[0])) / 2
        else:
            return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
