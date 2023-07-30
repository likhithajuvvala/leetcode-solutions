# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        length,tail=1,head
        while tail.next:
            tail=tail.next
            length+=1
        k=k%length
        tail.next=head
        newHead=head
        for i in range(length-k-1):
            newHead=newHead.next
        ans=newHead.next
        newHead.next=None
        return ans
