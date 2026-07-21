class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count =0
        sum = 0
        Map ={0:1}
        for i in nums:
            sum = sum+i
            if (sum % k) in Map:
                count += Map[sum % k] # Increase by value of key
                Map[sum % k] += 1
            
            else:
                Map[sum % k] = 1
        return count
            

