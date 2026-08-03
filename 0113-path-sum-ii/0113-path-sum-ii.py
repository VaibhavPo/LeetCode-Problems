# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans=[]
        def helper (root,total,subset):
            if  root is None :
                return
            if root.right is None and root.left is None:
                Sum = total+root.val
                if Sum == targetSum:
                    subset.append(root.val)
                    # print("HH", subset)
                    ans.append(subset[:])
                    # print("ANS", ans)
                    subset.pop()
                     
                return

            subset.append(root.val)
            helper(root.left, total+root.val, subset)
            subset.pop()
            subset.append(root.val)
            helper(root.right, total+root.val, subset)
            subset.pop()
            # print(subset, " ", total)

            

        helper(root,0,[])
        return ans