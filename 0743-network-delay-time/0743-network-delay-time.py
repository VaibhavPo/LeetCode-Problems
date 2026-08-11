import heapq
import sys
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        d = [sys.maxsize] * (n+1)
        aj_list = [[] for i in range(n+1)]
        heap = []

        for m,n,o in times:
            aj_list[m].append([o,n])

        heapq.heappush(heap,[0, k])
        d[k] = 0

        while len(heap) > 0:

            dis, node = heapq.heappop(heap)
            if dis > d[node]:
                continue
            for i,j in aj_list[node]:
                if (i + dis) < d[j]:
                    d[j] = i + dis
                    heapq.heappush(heap, [d[j], j])
        
        d.sort(reverse=True)
        print (d)
        if d[1] != sys.maxsize:
            return d[1]
        else:
            return -1
                

            



        