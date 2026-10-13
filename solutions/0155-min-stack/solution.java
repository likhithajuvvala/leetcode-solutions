class MinStack {

    private static class Node {
        int val;
        int min;
        Node next;

        Node(int val, int min, Node next) {
            this.val = val;
            this.min = min;
            this.next = next;
        }
    }

    private Node head;                     // the top plate

    public MinStack() {
    }

    public void push(int val) {
        if (head == null) {
            head = new Node(val, val, null);                       // first plate
        } else {
            head = new Node(val, Math.min(val, head.min), head);   // new top plate
        }
    }

    public void pop() {
        head = head.next;                  // drop the top plate
    }

    public int top() {
        return head.val;
    }

    public int getMin() {
        return head.min;
    }
}