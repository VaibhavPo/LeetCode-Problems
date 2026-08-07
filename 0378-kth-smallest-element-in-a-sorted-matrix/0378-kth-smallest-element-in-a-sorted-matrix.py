import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap_in = []
        n =  len(matrix)
        for i in matrix:
            for j in i:
                if len(heap_in) < k:
                   heapq.heappush(heap_in, -j)
                else:
                    if j < -heap_in[0]:
                        heapq.heapreplace(heap_in, -j)
        return(-heap_in[0])
        


