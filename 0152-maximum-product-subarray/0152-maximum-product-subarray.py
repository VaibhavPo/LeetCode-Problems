class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi =float('-inf')
        left =1
        right =1
        for i in range(len(nums)):
            left = left * nums[i]
            right = right * nums[len(nums)-i-1]
            maxi =max(maxi, left, right)
            if left ==0:
                left = 1
            if right ==0:
                right = 1
        return maxi