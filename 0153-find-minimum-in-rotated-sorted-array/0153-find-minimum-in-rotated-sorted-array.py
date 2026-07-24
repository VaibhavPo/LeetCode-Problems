class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while l<r:
            mid  = (l+r)// 2
            if nums[mid] > nums[r]: # This confirms that the left part is totally shorted
                l = mid + 1
            else:                   # This confirms that the right part is totally shorted
                r = mid
        return nums[l]

                