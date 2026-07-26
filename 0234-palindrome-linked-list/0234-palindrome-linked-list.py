# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        fast = head
        slow = head
        while fast != None and fast.next != None  :
            fast = fast.next.next
            slow = slow.next
        if fast != None: #odd number of elements
            slow = slow.next
        
        #reverse from slow
        temp = slow
        prev = None
        while temp is not None:    
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front    
        slow = prev
        fast = head
        while slow != None:
            if slow.val == fast.val:
                slow = slow.next
                fast = fast.next
            else:
                return False
        return True
            

        