# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr,itr=[],head
        while itr:
            arr.append(itr.val)
            itr=itr.next
        arr.sort()
        itr,i=head,0
        while itr:
            itr.val=arr[i]
            i+=1
            itr=itr.next
        return head
        
        