class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1. Store the original indices before sorting
        # We create pairs of (value, original_index)
        indexed_nums = []
        for index, value in enumerate(nums):
            indexed_nums.append((value, index))
        
        # 2. Sort based on the values
        indexed_nums.sort()
        
        # 3. Use two pointers
        left = 0
        right = len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                # Return the original indices
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1  # Need a larger sum
            else:
                right -= 1 # Need a smaller sum