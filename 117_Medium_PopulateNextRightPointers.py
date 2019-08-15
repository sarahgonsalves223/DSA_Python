"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        q = deque([])
        q.append(root)
        while len(q) > 0:
            level = deque([])
            prev = None
            while len(q) > 0:
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            node.next = None
            q = level
        return root

