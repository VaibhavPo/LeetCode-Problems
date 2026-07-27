class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        i = 0
        ans=set()
        nums.sort()
        n =len(nums)
        for i in range(n - 3):
            for j in range(i+1,n - 2):
                total = target - (nums[i]+nums[j])
                p = j+1
                q = n-1
                while p < q:
                    net = nums[p]+nums[q]-total
                    if net == 0:
                        ans.add((nums[i], nums[j], nums[p], nums[q]))
                        p += 1  # Move pointers so the while loop doesn't hang!
                        q -= 1
                    elif net > 0:
                        q -= 1
                    else:
                        p += 1
        return [list(quad) for quad in ans]


        