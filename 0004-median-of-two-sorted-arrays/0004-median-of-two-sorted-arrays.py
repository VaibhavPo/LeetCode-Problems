class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float        
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n = len(nums1)
        m = len(nums2)


        low=0
        high=n       

        while (low <= high):
            par1 = (low + high) // 2
            par2 = (m+n)//2 - par1
            l1= float('-inf') if par1 == 0 else nums1[par1 -1]
            l2= float('-inf') if par2 == 0 else nums2[par2 -1]
            r1= float('inf') if par1 == n else nums1[par1]
            r2 = float('inf') if par2 == m else nums2[par2]

            if (l1<=r2) and l2<=r1:
                if (m+n)%2 ==0:
                    return (float((max(l1,l2)+min(r2,r1))/2.0))
                else:
                    return (float(min(r2,r1)))
            elif (l1 > r2):
                high = par1 -1
            else:
                low = par1 + 1