class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0,float('-inf'))
        nums.append(float('-inf'))
        l = 0
        r = len(nums) -1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid-1
            elif nums[mid]< nums[mid-1]: # move to left
                r = mid -1 
            elif nums[mid] < nums[mid+1]:
                l = mid +1

