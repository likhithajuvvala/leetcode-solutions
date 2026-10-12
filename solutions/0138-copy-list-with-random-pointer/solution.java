/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if(head==null) return null;
        Map<Node,Node> mpp=new HashMap<>();
        Node cur=head;
        while(cur!=null){
            mpp.put(cur,new Node(cur.val));
            cur=cur.next;
        }
        cur=head;
        while(cur!=null){
            mpp.get(cur).next=mpp.get(cur.next);
            mpp.get(cur).random=mpp.get(cur.random);
            cur=cur.next;
        }
        return mpp.get(head);
    }
}