# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head:ListNode = None 
        while head:
            if new_head is None:
                new_head = ListNode(val=head.val, next=None)
            else:
                new_head = ListNode(val=head.val, next=new_head)
            head = head.next
        
        return new_head 
            
        