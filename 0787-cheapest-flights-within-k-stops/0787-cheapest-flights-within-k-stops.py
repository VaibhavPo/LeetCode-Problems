from collections import deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        vis =[float('inf')]*n
        q = deque()
        adj_l = [[]for i in range(n)]
        for a, node, cost in flights:
            adj_l[a].append([1, cost, node])
        # print(adj_l)

        q.append([0,0,src])
        vis[src] = 0
        while q:
            stop, c, no = q.popleft()
            
            for i in adj_l[no]:
                d, e, f = i
                if stop + d <= k+1 and vis[f] > e +c:
                    vis[f] = e+c
                    q.append([stop+d, e+c, f])
        # print(vis)
        if vis[dst] == float('inf'):
            return -1 
        return vis[dst]






        