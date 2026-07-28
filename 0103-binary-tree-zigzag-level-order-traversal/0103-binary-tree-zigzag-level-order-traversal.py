# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans=[]
        queue = deque([root])
        if not root:
            return []
        while queue:
            curr_level =[]
            for i in range(len(queue)):
                node = queue.popleft()
                curr_level.append(node.val)
                # Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            
            ans.append(curr_level)
        for i in range(len(ans)):
            if i%2 ==1:
                ans[i].reverse() 

        return ans