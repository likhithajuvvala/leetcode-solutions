class Solution {
    public int evalRPN(String[] tokens) {
         Deque<Integer> stack = new ArrayDeque<>();

        for (String t : tokens) {
            if (t.equals("+")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a + b);
            } else if (t.equals("-")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a - b);
            } else if (t.equals("*")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a * b);
            } else if (t.equals("/")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a / b);
            } else {
                stack.push(Integer.parseInt(t));   // it's a number
            }
        }
        return stack.pop();
    }
}