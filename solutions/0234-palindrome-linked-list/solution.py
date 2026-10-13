# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        op=[]
        p=head
        while p!=None:
            op.append(p.val)
            p=p.next
        return op==op[::-1]