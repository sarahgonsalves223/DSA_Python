#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (31.61%)
# Total Accepted:    976.3K
# Total Submissions: 3.1M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l3 = ListNode(0)
        head = l3
        carry = 0
        while l1 or l2:
            value = 0
            if l1:
                value += l1.val
            if l2:
                value += l2.val
            if carry:
                value +=1
            node = ListNode(value%10)
            l3.next = node
            carry = int(value/10)
            l3 = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            l3.next = ListNode(carry)
        return head.next
            
            
                
            
