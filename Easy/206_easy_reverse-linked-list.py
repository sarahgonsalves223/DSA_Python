#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (56.17%)
# Total Accepted:    650.8K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        
        while head:
            stack.append(head)
            head = head.next
        
        node = ListNode(-1)
        head = node
        while len(stack) > 0:
            node.next = stack.pop()
            node = node.next
        node.next = None
        return head.next
            
