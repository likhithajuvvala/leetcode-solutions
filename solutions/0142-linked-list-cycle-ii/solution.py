# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        if not head:
            return None
        if head.next==head:
            return head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while fast.next!=slow:
                    slow=slow.next
                    if fast.next!=slow:
                        fast=fast.next
                    else:
                        if fast==head:
                            return fast
                        else:
                            return slow
                        
                






