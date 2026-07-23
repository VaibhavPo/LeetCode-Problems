class Solution(object):
    def upB(self,nums,target):
        l = 0
        r = len(nums) -1
        UB = len(nums)
        while l<=r:
            mid = (l+r)//2
            if target < nums[mid]:
                UB = mid
                r = mid - 1
            else:
                l = mid+1
        return UB
    
    def lwB(self,nums,target):# For calculating lower bound
        l = 0
        r = len(nums) -1
        LB = -1
        while l<=r:
            mid = (l+r)//2
            if target <= nums[mid]:
                LB = mid
                r = mid -1
            else:
                l = mid+1
        if LB != -1 and nums[LB] == target:
            return LB        
        return -1


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lower = self.lwB(nums, target)
        if lower == -1 :
            return [-1,-1]
        else:
            upper = self.upB(nums, target)
           

        return [lower, upper-1]

    