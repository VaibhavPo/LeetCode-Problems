import heapq as hp
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap = []
        ans =[]
        for i in range(len(arr)):
            if i < k:
                hp.heappush(heap,( -abs(arr[i] - x), -arr[i]))
            else:
                m, n = heap[0]
                if  m < ( -abs(arr[i] - x)) :
                    hp.heapreplace(heap, ( -abs(arr[i] - x), -arr[i] ))

        for w, z in heap:          
            ans.append(-z)
        # print(ans)
        ans.sort()
        return ans

            

        