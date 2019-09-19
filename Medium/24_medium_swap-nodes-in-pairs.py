#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (45.91%)
# Total Accepted:    355.5K
# Total Submissions: 767.2K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = self.helper(head)
        return new_head
    
    def helper(self, node: ListNode) -> ListNode:
        if not node or not node.next:
            return node
        two = node.next
        three = two.next
        if three:
            three = self.helper(three)
        node.next = three
        two.next = node
        return two
