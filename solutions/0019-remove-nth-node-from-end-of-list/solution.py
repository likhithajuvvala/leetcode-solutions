# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None :
            return None
        slow=fast=head
        for i in range(1,n):
            fast= fast.next
        while fast.next!=None:
            fast= fast.next
            slow=slow.next
        if slow==head:
            head=head.next
            return head
        p=head
        while p.next!=slow:
            p=p.next
        p.next=slow.next
        return head
        
        

        
        