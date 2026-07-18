# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        #Approach with space complexity of O(N)
        """
        visited=set()
        current = head
        while current != None:
            if current in visited:
                return True

            visited.add(current)
            current=current.next
        return False 
        """
        #Improved Version: Floyd’s Cycle Detection
        fast=head
        slow=head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False