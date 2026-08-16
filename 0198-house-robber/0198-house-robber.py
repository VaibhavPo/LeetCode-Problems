class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
            
        # n = len(nums)
        # # We only need an array of size n to store the states
        # nb = [-1] * n
        
        # def find(a):
        #     # Base cases: return immediately
        #     if a == 0:
        #         return nums[0]
        #     if a == 1:
        #         return max(nums[1], nums[0])
                
        #     # Return memoized result if already calculated
        #     if nb[a] != -1: 
        #         return nb[a]
                
        #     # The core logic: Max of (rob current + rob a-2) OR (skip current and rob a-1)
        #     nb[a] = max(find(a-2) + nums[a], find(a-1))
        #     return nb[a]

        # return find(n - 1)

        n =len(nums)
        if n <= 1:
            return nums[0]
        nb = [-1] *n
        nb[0] = nums[0]
        nb[1] = max(nums[0],nums[1])
        for i in range(2, n):
            find = max(nums[i] + nb[i-2], nb[i-1])
            nb[i] = find
        return nb[-1]
