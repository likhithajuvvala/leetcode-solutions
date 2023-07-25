# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
             return None
        prev=None
        curr=head
        n=curr.next
        while curr!=None:
            curr.next=prev
            prev=curr
            curr=n
            if n!=None:
                n=n.next
            head=prev
        return head
        
        