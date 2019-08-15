#
# @lc app=leetcode id=951 lang=python
#
# [951] Flip Equivalent Binary Trees
#
# https://leetcode.com/problems/flip-equivalent-binary-trees/description/
#
# algorithms
# Medium (64.83%)
# Total Accepted:    19.7K
# Total Submissions: 30.3K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]'
#
# For a binary tree T, we can define a flip operation as follows: choose any
# node, and swap the left and right child subtrees.
# 
# A binary tree X is flip equivalent to a binary tree Y if and only if we can
# make X equal to Y after some number of flip operations.
# 
# Write a function that determines whether two binary trees are flip
# equivalent.  The trees are given by root nodes root1 and root2.
# 
# 
# 
# Example 1:
# 
# 
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =
# [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
# 
# 
# 
# 
# 
# Note:
# 
# 
# Each tree will have at most 100 nodes.
# Each value in each tree will be a unique integer in the range [0, 99].
# 
# 
# 
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == root2:
            return True
        elif root1 == None or root2 == None:
            return False
        else:

            if root1.left != None and root2.left != None and root1.right != None and root2.right != None:
                if root1.left.val == root2.right.val and root1.right.val == root2.left.val:
                    temp = root1.left
                    root1.left = root1.right
                    root1.right = temp
                if root1.left.val == root2.left.val and root1.right.val == root2.right.val:
                    return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
                else:
                    return False
            else:
                if root1.left == None and root2.left == None and root1.right == None and root2.right == None:
                    return True
                elif root1.left == None and root2.left == None and root1.right != None and root2.right != None:
                    if root1.right.val != root2.right.val:
                        return False
                    else:
                        return self.flipEquiv(root1.right, root2.right)
                elif root1.left != None and root2.left != None and root1.right == None and root2.right == None:
                    if root1.left.val != root2.left.val:
                        return False
                    else:
                        return self.flipEquiv(root1.left, root2.left)
                elif root1.left == None and root2.right == None:
                    if root1.right == None and root2.left == None:
                        return True
                    elif root1.right == None or root2.left == None:
                        return False
                    elif root1.right.val == root2.left.val:
                        temp = root1.left
                        root1.left = root1.right
                        root1.right = temp
                        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
                    else:
                        return False
                elif root1.right == None and root2.left == None:
                    if root1.left == None and root2.right == None:
                        return True
                    elif root1.left == None or root2.right == None:
                        return False
                    elif root1.left.val == root2.right.val:
                        temp = root1.left
                        root1.left = root1.right
                        root1.right = temp
                        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
                    else:
                        return False
                else:
                    return False
        return True
        

