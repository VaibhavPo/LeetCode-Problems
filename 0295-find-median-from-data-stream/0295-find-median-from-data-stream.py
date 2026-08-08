import heapq
class MedianFinder(object):

    def __init__(self):
        self.heapL = []
        self.heapR = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.heapL:
            heapq.heappush(self.heapL, -num)

        elif num <= -self.heapL[0]:
            heapq.heappush(self.heapL, -num)

        else:
            heapq.heappush(self.heapR, num)

        
        # Keep left at most one element larger than right
        if len(self.heapL) > len(self.heapR) + 1:
            item = -heapq.heappop(self.heapL)
            heapq.heappush(self.heapR, item)
        
        elif len(self.heapR) > len(self.heapL):
            item =  heapq.heappop(self.heapR)
            heapq.heappush(self.heapL, -item)


    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.heapR) + len(self.heapL))%2 ==0:
            return (-self.heapL[0] + self.heapR[0]) / 2.0
        else:
            return -self.heapL[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()