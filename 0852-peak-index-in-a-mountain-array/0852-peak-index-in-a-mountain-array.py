class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = 0
        r = len(arr)-1
        while l<r:
            mid  = (l+r)// 2
            if arr[mid] > arr[mid+1]:
                r = mid #mid can also be the peak
            else:
                l = mid+1
        return l        