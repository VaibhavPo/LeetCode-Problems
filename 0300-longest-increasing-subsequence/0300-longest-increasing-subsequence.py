class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        l = [1] * n
        
        for i in range(n):
            for j in range(i+1):
                if nums[i] > nums[j]:
                    if l[i] < l[j] + 1:
                        l[i] = l[j] + 1
                # else:
        return max(l)

