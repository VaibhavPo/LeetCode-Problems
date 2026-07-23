# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        a = head
        i=1
        br1 = None
        br2 = None
       
        while a  != None:
            
            if i < left:
                br1 = a
                a= a.next
                
            if i == left:  
                br2 = a
                prev = None
                
                

            if i >= left and i <= right:
                front = a.next
                a.next = prev
                prev = a
                a = front
            if i == right:
                if br1:
                    br1.next = prev
                else:
                    head = prev
                br2.next = a
                
            if  i >right:
                a = a.next

            i += 1
        return head
