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
    int good=0;
    public void dfs(TreeNode node, int val){
        if(node==null) return;
        if(node.val>=val){
            good++;
            val=node.val;
        }
        dfs(node.left,val);
        dfs(node.right,val);
    }
    public int goodNodes(TreeNode root) {
        dfs(root,root.val);
        return good;
    }
}
