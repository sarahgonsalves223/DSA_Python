#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (37.52%)
# Total Accepted:    216.5K
# Total Submissions: 562.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Time complexity = O(n)
        Space Complexity = O(1)
        """
        n = 1
        dummy = head
        while dummy and n < k:
            n += 1
            dummy = dummy.next
            
        if n < k or not dummy:
            return head
        else:
            next_head = dummy.next
            dummy.next = None
            next_head = self.reverseKGroup(next_head, k)
            arr = self.reverse(head)
            head, tail = arr[0], arr[1]
            tail.next = next_head
            return head
    
    def reverse(self, head):
        if not head or not head.next:
            return head,head
        dummy_next = head.next
        head.next = None
        arr = self.reverse(dummy_next)
        new_head, new_tail = arr[0], arr[1]
        if new_tail:
            new_tail.next = head
        return [new_head, head]
            
            
