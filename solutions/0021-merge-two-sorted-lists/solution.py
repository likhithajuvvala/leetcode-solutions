# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        op=[]
        r=list1
        while r.next!=None:
            r=r.next
        r.next=list2
        p=list1
        while p!=None:
            op.append(p.val)
            p=p.next
        op.sort()
        p=list1
        for i in op:
            p.val=i
            p=p.next
        return list1