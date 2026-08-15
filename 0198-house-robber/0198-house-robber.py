# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         nb = [-1]*(n+1)
        
#         t = 0
#         def find(a,t):
#             if (a == 0):
#                 t += nums[0]
#             elif  a==1:
#                 t += max(nums[1], nums[0])
#             else:
#                 x,y = nb[a-2], nb[a-1]
#                 if x != -1:
#                    t += max(x + nums[a], find(a-1,t)) 
#                 elif y != -1:
#                     t += max(find(a-2,t) + nums[a], y)
#                 else:
#                     t += max(find(a-2,t) + nums[a], find(a-1,t))
#                 nb[a] = t
#             return t

#         return find(n-1,t)

class Solution(object):
    def rob(self, nums):
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        nb = [-1] * n

        def find(a):
            if a == 0:
                return nums[0]

            if a == 1:
                return max(nums[0], nums[1])

            if nb[a] != -1:
                return nb[a]

            nb[a] = max(find(a-2) + nums[a], find(a-1))
            return nb[a]

        return find(n-1)