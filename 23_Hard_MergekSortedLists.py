"""
Question:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        for i,ls in enumerate(lists):
            if ls:
                pq.append((ls.val, i))
                lists[i] = ls.next
        
        heapq.heapify(pq)
        head = ListNode(-1)
        prev = head
        while pq:
            value, index = heapq.heappop(pq)
            node = ListNode(value)
            prev.next = node
            prev = node
            next_list = lists[index]
            if next_list:
                heapq.heappush(pq, (next_list.val, index))
                lists[index] = next_list.next
        return head.next
