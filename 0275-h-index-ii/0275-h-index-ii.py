class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        minH = 0
        maxH = len(citations)-1
 
        while minH <= maxH:
            mid = (minH + maxH)//2
            if citations[mid] >= len(citations) - mid:
                maxH = mid -1
            else:
                minH = mid +1
        return len(citations) - minH

            
