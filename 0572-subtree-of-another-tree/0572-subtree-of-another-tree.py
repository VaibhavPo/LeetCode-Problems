# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        arr1= []
        arr2=[]
        def traversal(root,arr):
            arr.append("," + str(root.val))
            if root.left:
                traversal(root.left, arr)
            else:
                arr.append('#')
            if root.right:
                traversal(root.right, arr)
            else:
                arr.append('#') 

        traversal(root,arr1)
        traversal(subRoot,arr2)

        
        # print (s1, " sg", s2) 

        return join(arr2) in join(arr1)             
