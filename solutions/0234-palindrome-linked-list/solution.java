/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
       ListNode fast=head,slow=head;
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        //if the ll size is odd 
        if(fast!=null){
            slow=slow.next;
        }
        slow=reverseList(slow);//right half ll
        fast=head;//left half ll

        // compare two lls
        while(slow!=null){
           if(fast.val!=slow.val)
                return false;
        
            fast=fast.next;
            slow=slow.next;
        }
        return true;
    }
    public ListNode reverseList(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode prevNode=head;
        ListNode currNode=head.next;
        while(currNode!=null){
            ListNode nextNode=currNode.next;
            currNode.next=prevNode;//does the reversing part
 
            //update
            prevNode=currNode;
            currNode=nextNode;
        }
        head.next=null;
        head=prevNode;
        return head;
    }
}