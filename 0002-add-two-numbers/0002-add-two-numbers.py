# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sk1=[]
        sk2=[]
        sk_r=[]
        carry = 0
        while l1 is not None or l2 is not None or carry !=0: 
            
            sk1.append(l1.val if l1 is not None else 0)
            sk2.append(l2.val if l2 is not None else 0)
            sum =(sk1.pop() + sk2.pop() + carry)
            if sum <10:
                sk_r.append(sum) 
                carry =0   
            else:
                sk_r.append(sum % 10) 
                carry =1   

            if l1 is not None:
                l1 =l1.next
            if l2 is not None:
                l2 =l2.next
        
        head = ListNode(sk_r[0])
        tail =head

    
        for i in sk_r[1:]:
            # Create a new node and link it to the tail
            new_node = ListNode(i)
            tail.next = new_node
            
            # Move the tail pointer to the newly created node
            tail = new_node            
        return head
            

        


