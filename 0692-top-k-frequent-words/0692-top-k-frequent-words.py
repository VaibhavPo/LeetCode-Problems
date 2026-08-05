import collections
import heapq as hp

class Heapitem:

    def __init__(self, word, count) :
        self.word = word
        self.count = count

    def __lt__(self, to_compare) :
        if self.count == to_compare.count:
            return self.word > to_compare.word
        else:
            return self.count < to_compare.count


class Solution(object):

    def topKFrequent(self, words, k):
        """:type words: List[str]

        :type k: int
        :rtype: List[str]
        """
        coll = collections.Counter(words)
        heap = []
        
        for word, count in coll.items():
            item = Heapitem(word, count)
            if len(heap) < k:
                hp.heappush(heap, item)
            else:
                if heap[0] < item:
                    hp.heapreplace(heap, item)
        # print[heap]
        res=[]
        for i in range(0,k):
            res.append(hp.heappop(heap).word)
        return res[::-1]

