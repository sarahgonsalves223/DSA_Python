from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        count = Counter(nums1)
        for num in nums2:
            if num in count and count[num] > 0:
                count[num] = count[num] - 1
                ans.append(num)
        return ans