import heapq
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        stations.append([target, 0])
        fuel = startFuel
        count = 0
        heap = []
        prev =0
        for position, fu in stations:
            dis = position - prev

            fuel = fuel - dis

            while fuel < 0:      
                if len(heap) > 0:                                
                    fuel += - heapq.heappop(heap)
                    count += 1
                else:
                    return -1
            heapq.heappush(heap, -fu)
            prev = position
        
        return count

            









            