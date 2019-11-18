#
# @lc app=leetcode id=428 lang=python
#
# [428] Serialize and Deserialize N-ary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/description/
#
# algorithms
# Hard (55.04%)
# Total Accepted:    20.3K
# Total Submissions: 36K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree
# is a rooted tree in which each node has no more than N children. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that an N-ary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# For example, you may serialize the following 3-ary tree
# 
# 
# 
# 
# 
# 
# 
# as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format, so
# please be creative and come up with different approaches yourself.
# 
# 
# 
# Note:
# 
# 
# N is in the range of  [1, 1000]
# Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
# 
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        order = []
        def preorder(node):
            if not node:
                return
            order.append(str(node.val))
            for child in node.children:
                preorder(child)
            order.append("#")
            return
        
        preorder(root)
        return " ".join(order)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        
        stack = []
        nodes = data.split(" ")
        if not nodes[0]:
            return None
        root = Node(int(nodes[0]), [])
        stack.append(root)
        i = 1
        while stack:
            next_node = nodes[i]
            if next_node == "#":
                stack.pop()
            else:
                node = Node(int(next_node), [])
                stack[-1].children.append(node)
                stack.append(node)
            i += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
