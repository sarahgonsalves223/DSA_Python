"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)

    def helper(self, root):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left == None or root.right == None:
            return 2
        else:
            complete, height = self.isComplete(root.left)
            if complete:
                left_size = 2**(height+1) - 1
                right_size = self.helper(root.right)
                return left_size + right_size + 1
            else:
                left_size = self.helper(root.left)
                right_size = 2**(height+1) - 1
                return left_size + right_size + 1

    def isComplete(self, root):
        node = root
        hl = 0
        while node.left:
            hl = hl + 1
            node = node.left
        node = root
        hr = 0
        while node.right:
            hr = hr + 1
            node = node.right
        return (hl == hr), hr

