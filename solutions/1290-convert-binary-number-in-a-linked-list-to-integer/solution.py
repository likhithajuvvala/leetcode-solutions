# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=[]
        p=head
        while p!=None:
            s.append(p.val)
            p=p.next
        num=0
        s=s[::-1]
        for i in range(len(s)):
            num+=s[i]*2**i

        return num



        