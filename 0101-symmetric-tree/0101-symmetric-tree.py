# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        leftQ= deque([root.left])
        rightQ= deque([root.right])

        while leftQ and rightQ:
            if (len(leftQ) != len(rightQ)):
                return False
            for i in range(len(leftQ)):
                nodeL = leftQ.popleft()
                nodeR = rightQ.popleft()
                
                if not nodeL and not nodeR:
                    continue
                elif  (nodeL and not nodeR) or (not nodeL and  nodeR):
                    return False
                elif  nodeL.val != nodeR.val:
                    return False
                
                
                leftQ.append(nodeL.left)
                rightQ.append(nodeR.right)
                
                leftQ.append(nodeL.right)
                rightQ.append(nodeR.left)
        return True



        