class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)/2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]: #Left part shorted
            # If fixed in left part
                if nums[l]  <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
            else: #Right part shorted
                if nums[mid] < target <= nums[r]:
                    l = mid +1 
                else:
                    r = mid -1       
        return -1

        