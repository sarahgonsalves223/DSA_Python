#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (26.77%)
# Total Accepted:    333.5K
# Total Submissions: 1.2M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#
class ListNode:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = None
        self.prev = None
    
    def print(self):
        print([self.key, self.val])

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]
            node = ListNode(key,value)
            self.cache[key] = node
            self.add(node)
        elif len(self.cache) >= self.capacity:
            #evict from the ll and cache
            tail = self.tail
            self.remove(self.tail)
            del self.cache[tail.key]
            #put new node in the cache and ll
            node = ListNode(key,value)
            self.cache[key] = node
            self.add(node)
        else:
            node = ListNode(key,value)
            self.cache[key] = node
            self.add(node)
    
    def add(self, node: ListNode) -> None:
        #add the node to the front
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            
        if not self.tail:
            self.tail = node
        
    def remove(self, node) -> int:
        #remove the node
        prev = node.prev
        nxt = node.next
        if prev:
            prev.next = nxt
        if nxt:
            nxt.prev = prev
        if node == self.tail:
            self.tail = prev
        if node == self.head:
            self.head = nxt
        node.prev = None
        node.next = None
        return node.key

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
