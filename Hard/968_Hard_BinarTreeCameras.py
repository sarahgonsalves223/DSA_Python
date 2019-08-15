"""
Question:
Given a binary tree, we install cameras on the nodes of the tree. 
Each camera at a node can monitor its parent, itself, and its immediate children.
Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:
Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:
Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        self.covered = set()
        self.covered.add(None)
        self.dfs(root)
        return self.ans
        
    def dfs(self, root, par = None):
        if root:
            self.dfs(root.left, root)
            self.dfs(root.right, root)

            if (par == None and root not in self.covered) or (root.left not in self.covered or root.right not in self.covered):
                self.ans += 1
                self.covered.add(root) 
                self.covered.add(root.right)
                self.covered.add(root.left)
                self.covered.add(par)


