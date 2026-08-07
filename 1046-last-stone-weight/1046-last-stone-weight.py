import heapq as hp
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        # for i in stones:
        #     heap.append(-i)
        # hp.heapify(heap)
        heap = [-stone for stone in stones]
        hp.heapify(heap)
        while len(heap) > 1:
            y = -hp.heappop(heap)    
            x = -hp.heappop(heap)

            if x != y:
                hp.heappush(heap, -(y-x))
            else:
                hp.heappush(heap,0)
        return(-hp.heappop(heap))
        