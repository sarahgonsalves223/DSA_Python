#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (28.25%)
# Total Accepted:    266.5K
# Total Submissions: 943.6K
# Testcase Example:  '{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer
# points to itself.
# 
# 
# 
# 
# Note:
# 
# 
# You must return the copy of the given head as a reference to the cloned
# list.
# 
# 
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        node_table = {}
        head2 = Node(-1, None, None)
        while head:
            if head.next:
                if head.next.val in node_table:
                    next_node = node_table[head.next.val]
                else:
                    next_node = Node(head.next.val, None, None)
                    node_table[head.next.val] = next_node
            else:
                next_node = None
                
            if head.random:
                if head.random.val in node_table:
                    random_node = node_table[head.random.val]
                else:
                    random_node = Node(head.random.val, None, None)
                    node_table[head.random.val] = random_node
            else:
                random_node = None
            
            if head.val in node_table:
                node = node_table[head.val]
                node.next = next_node
                node.random = random_node
            else:
                node = Node(head.val, next_node, random_node)
                node_table[head.val] = node
            
            if head2.next == None:
                head2.next = node
                
            head = head.next
        return head2.next
                
            
        
