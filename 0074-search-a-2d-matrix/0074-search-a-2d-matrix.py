class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        small, large = 0, len(matrix)-1
        l, r= 0, len(matrix[0])-1
        row= -1       

        while small <= large:
            center = (small+large)//2
            if target == matrix[center][0]:
                return True

            if target > matrix[center][0]:
                row = center
                small = center + 1
            else:
                large = center -1
        if row == -1:
            return False
        print(row)

        while l<= r:
            mid = (l+r)//2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid +1
            else:
                r = mid-1
        return False
