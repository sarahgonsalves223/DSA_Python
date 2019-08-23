class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i,ch in enumerate(s):
            num += (ord(ch)-64)*(26**(len(s) - i - 1))
        return num