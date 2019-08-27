#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (34.51%)
# Total Accepted:    437.4K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
# 
# Example:
# 
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        fast = head
        leng = 0
        while fast:
            fast = fast.next
            leng += 1
        if leng == n:
            return head.next
        leng = leng - n
        fast = head
        while leng > 1:
            fast = fast.next
            leng -= 1
        fast.next = fast.next.next
        #slow.next.next = None
        return head
        
