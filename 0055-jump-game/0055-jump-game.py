class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_ind = 0
        for i in range(n):
            if max_ind < i:
                return False
            else:
                if max_ind < nums[i] + i:
                    max_ind = nums[i] +i
        return True