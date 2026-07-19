class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max =float('-inf')
        total = 0
        for i in nums:
            total = total + i
            if total > max:
                max = total
            if total < 0:
                total = 0
        return max

