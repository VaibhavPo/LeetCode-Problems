class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        Brute force
        count=0
        for idx,i in enumerate(nums):
            sum =0            
            for j in nums[idx:]:                
                sum = sum+j
                if sum  == k:
                    count = count + 1                   
                    break
                
            return count
                 """
        count =0
        SumDic ={0:1}
        sum =0
        for i in nums:
            sum += i
            if (sum - k) in SumDic:
                count += SumDic[sum-k]
                
            if sum in SumDic:
                SumDic[sum] += 1
            else:
                SumDic[sum] = 1
        return count
            