class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nb = [-1]*(n+1)
        
        t = 0
        def find(a,t):
            if (a == 0):
                t += nums[0]
            elif  a==1:
                t += max(nums[1], nums[0])
            else:
                x,y = nb[a-2], nb[a-1]
                if x != -1:
                   t += max(x + nums[a], find(a-1,t)) 
                elif y != -1:
                    t += max(find(a-2,t) + nums[a], y)
                else:
                    t += max(find(a-2,t) + nums[a], find(a-1,t))
                nb[a] = t
            return t

        return find(n-1,t)

