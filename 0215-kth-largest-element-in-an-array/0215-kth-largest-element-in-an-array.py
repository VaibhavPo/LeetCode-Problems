import heapq as hp
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # n = len(nums)
        
        # # Helper function to sink an element down the tree
        # def sift_down(ind,n):
        #     largest = ind
        #     left = 2 * ind + 1
        #     right = 2 * ind + 2
            
        #     # Check if left child exists and is greater than current largest
        #     if left < n and nums[left] > nums[largest]:
        #         largest = left
                
        #     # Check if right child exists and is greater than current largest
        #     if right < n and nums[right] > nums[largest]:
        #         largest = right
                
        #     # If the largest is not the current index, swap and continue sifting down
        #     if largest != ind:
        #         nums[ind], nums[largest] = nums[largest], nums[ind]
        #         sift_down(largest,n)

        # # Start from the last non-leaf node and go backwards to the root
        # for i in range((n // 2) - 1, -1, -1):
        #     sift_down(i,n)
        # print(nums)

        # last = n -1
         
        # for j in range(k):
        #     nums[0], nums[last] = nums[last], nums[0]
        #     Re_no = nums[last]
        #     sift_down(0,last)
        #     last -= 1

        # return(Re_no)
        heap =nums[:k]
        hp.heapify(heap)
        for i in nums[k:]:
            if i > heap[0]:
                hp.heapreplace(heap, i)
        return heap[0]






        