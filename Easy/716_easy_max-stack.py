#
# @lc app=leetcode id=716 lang=python3
#
# [716] Max Stack
#
# https://leetcode.com/problems/max-stack/description/
#
# algorithms
# Easy (40.60%)
# Total Accepted:    29K
# Total Submissions: 71.4K
# Testcase Example:  '["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]\n[[],[5],[1],[5],[],[],[],[],[],[]]'
#
# Design a max stack that supports push, pop, top, peekMax and popMax.
# 
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you
# find more than one maximum elements, only remove the top-most one.
# 
# 
# 
# Example 1:
# 
# MaxStack stack = new MaxStack();
# stack.push(5); 
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
# 
# 
# 
# Note:
# 
# -1e7 
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.
# 
# 
#
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.max_stack) > 0 and self.max_stack[-1] <= x:
            self.max_stack.append(x)
        if len(self.max_stack) == 0:
            self.max_stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            num = self.stack.pop()
            if num >= self.max_stack[-1]:
                self.max_stack.pop()
            return num
        else:
            return None

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def peekMax(self) -> int:
        if len(self.max_stack) > 0:
            return self.max_stack[-1]
        return None

    def popMax(self) -> int:
        maxi = self.max_stack.pop()
        temp = []
        while len(self.stack) > 0 and self.stack[-1] < maxi:
            temp.append(self.stack.pop())
        if len(self.stack) > 0 and self.stack[-1] == maxi:
            self.stack.pop()
        while len(temp) > 0:
            self.push(temp.pop())
        return maxi


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
