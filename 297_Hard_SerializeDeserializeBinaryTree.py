"""
Question:
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        chararray = []
        q = deque([])
        if root:
            q.append(root)
        else:
            chararray.append("#")
            return "".join(chararray)
        while len(q) > 0:
            node = q.popleft()
            if node:
                chararray.append(str(node.val))
                chararray.append(",")
                q.append(node.left)
                q.append(node.right)
            else:
                chararray.append("#")
                chararray.append(",")
        while chararray[-2] == "#" and chararray[-1] == ",":
            chararray = chararray[:-2]
        chararray = chararray[:-1]
        return "".join(chararray)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        chararray = data.split(",")
        if chararray[0] == "#":
            root = None
        else:
            root = TreeNode(int(chararray[0]))
            q = deque([])
            q.append(root)
            i = 1
            while i < len(chararray):
                node = q.popleft()
                if chararray[i] != "#":
                    left = TreeNode(chararray[i])
                    node.left = left
                    q.append(left)
                if i+1 < len(chararray) and chararray[i+1] != "#":
                    right = TreeNode(chararray[i+1])
                    node.right = right
                    q.append(right)
                i = i+2
        return root
    
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
