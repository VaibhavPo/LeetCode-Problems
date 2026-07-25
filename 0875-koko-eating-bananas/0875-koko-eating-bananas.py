class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        #Brute force approach
        
        # for k in range(1,max(piles)+1):
        #     time = 0
        #     for i in piles:
        #         time += -(i// -k)
        #     if time == h:
        #         return k
        #     elif time > h:
        #         pass
        #     else:
        #         continue

        slow = 1
        fast = max(piles)
        minSpeed = fast
        while slow <= fast:
            med = (slow + fast)// 2
            #Check at medium speed
            time = 0
            for i in piles:
                time += -(i// -med)
                if time > h:  
                    slow = med + 1              
                    break
            
            if time <= h: 
                minSpeed = med
                fast = med - 1
        return minSpeed

                

            




        