class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort(key = lambda x: len(x))
        common_str = ""
        for i in range(1, len(strs[0]) + 1):
            common_str = strs[0][0:i]
            for word in strs[1:]:
                if word.startswith(common_str):
                    continue
                else:
                    return common_str[:-1]
        return common_str
                