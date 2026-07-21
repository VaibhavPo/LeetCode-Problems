class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = 0
        rightSum = 0
        Sums=[]
        Sum = 0
        for i in nums:
            
            Sum += i
            Sums.append(Sum)

        
        totalSum = Sums[len(Sums)-1]
        
        for j in range(len(Sums)):
            rightSum = totalSum - Sums[j]
            if j != 0:
                leftSum = Sums[j-1]
            
            if leftSum == rightSum :
                return j
            leftSum = rightSum
            
         
        return -1