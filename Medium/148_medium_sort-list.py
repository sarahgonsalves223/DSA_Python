#
# @lc app=leetcode id=148 lang=python
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (36.71%)
# Total Accepted:    204.6K
# Total Submissions: 551.1K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        left, right = head, self.splitList(head)
        dum = left
        while dum.next != right:
            dum = dum.next
        dum.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        three = self.mergeLists(left, right)
        return three
        
    def splitList(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def mergeLists(self, one, two):
        three = ListNode(-1)
        three_head = three
        while one and two:
            if one.val < two.val:
                three.next = one
                one = one.next
            else:
                three.next = two
                two = two.next
            three = three.next
        if one:
            three.next = one
        if two:
            three.next = two
        return three_head.next

    def printy(self, head):
        dumm = head
        while dumm:
            dumm = dumm.next
            
        
