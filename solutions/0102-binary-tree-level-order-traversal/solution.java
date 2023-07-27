/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        List<List<Integer>> wrap = new LinkedList<List<Integer>>();
        if(root==null) return wrap;
        queue.add(root);
        while(!queue.isEmpty()){
            List<Integer> list = new LinkedList<>();
            int num = queue.size();
            for(int i=0; i<num; i++){
                if(queue.peek().left!=null) queue.add(queue.peek().left);
                if(queue.peek().right!=null) queue.add(queue.peek().right);
                list.add(queue.remove().val);
            }
            wrap.add(list);
        }
        return wrap;
        
    }
}