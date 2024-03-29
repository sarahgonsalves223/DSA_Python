#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/
#
# algorithms
# Medium (41.86%)
# Total Accepted:    50.4K
# Total Submissions: 114.7K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# Given a list accounts, each element accounts[i] is a list of strings, where
# the first element accounts[i][0] is a name, and the rest of the elements are
# emails representing emails of the account.
# 
# Now, we would like to merge these accounts.  Two accounts definitely belong
# to the same person if there is some email that is common to both accounts.
# Note that even if two accounts have the same name, they may belong to
# different people as people could have the same name.  A person can have any
# number of accounts initially, but all of their accounts definitely have the
# same name.
# 
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order.  The accounts themselves can be returned in any
# order.
# 
# Example 1:
# 
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
# 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
# "mary@mail.com"]]
# Explanation: 
# The first and third John's are the same person as they have the common email
# "johnsmith@mail.com".
# The second John and Mary are different people as none of their email
# addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary',
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
# would still be accepted.
# 
# 
# 
# Note:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
# 
#
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Time complexity = O(n^2)
        Space Complexity = O(n)
        """
        email_to_index = {}
        parent = [i for i in range(len(accounts))]
        for index, account in enumerate(accounts):
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email in email_to_index:
                    self.union(parent, email_to_index[email], index)
                else:
                    email_to_index[email] = index
        index_to_email = defaultdict(set)
        for i in range(len(accounts)):
            index = self.find(parent, i)
            emails = accounts[i][1:]
            index_to_email[index].update(emails)
        ans = []
        for index in index_to_email:
            name = accounts[index][0]
            emails = sorted(list(index_to_email[index]))
            curr = [name]
            curr.extend(emails)
            ans.append(curr)
        return ans
                    
    def find(self, parent, index):
        while parent[index] != index:
            index = parent[index]
        return index
    
    def union(self, parent, one, two):
        one = self.find(parent, one)
        two = self.find(parent, two)
        parent[one] = parent[two]

