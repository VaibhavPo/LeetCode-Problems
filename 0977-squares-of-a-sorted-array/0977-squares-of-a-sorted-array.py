class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        head= 0
        tail = len(nums)-1
        while head <= tail:   
            sqH = nums[head] * nums[head]
            sqT =  nums[tail] * nums[tail]
            if sqH < sqT:
                ans.insert(0, sqT)
                tail -= 1
            else:
                ans.insert(0, sqH)   
                head += 1           

        return (ans)
