# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p=head
        op=[]
        if not head:
            return None
        while p!=None:
            op.append(p.val)
            p=p.next
        k=k%len(op)
        op=op[len(op)-k:]+op[:len(op)-k]
        p=head
        for i in op:
            p.val=i
            p=p.next
        return head

