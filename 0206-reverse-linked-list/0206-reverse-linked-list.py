# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # a = head
        # # print (a)
        # b =[]
        
        # while a != None:
        #     b.append(a.val)
        #     a = a.next
        # print(b)

        # a = head
        # for i in range(len(b)):
        #     a.val = b.pop()
        #     a=a.next
        # return head

        #Optimal Approach
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        
        return prev
            
