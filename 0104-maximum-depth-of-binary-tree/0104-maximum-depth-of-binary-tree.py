# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # a = [0]
        # def Traversal(root,level):
        #     if root is None:
        #         level -= 1
        #         return 
        #     else:
        #         level += 1
        #         maxLevel = a[0]
        #         maxLevel = max (level, maxLevel)
        #         a.pop()
        #         a.append(maxLevel)
        #         Traversal(root.left, level )
        #         Traversal(root.right, level)
        #         # print(maxLevel)
        # Traversal(root, 0)
        # return a[0]

        def depth(node):
            if node is None:
                return 0
            
            LeftH = depth(node.left)
            RightH = depth(node.right)
            return 1 + max(LeftH, RightH)
        return depth(root) 
