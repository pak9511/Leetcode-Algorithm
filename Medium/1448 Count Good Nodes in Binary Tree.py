# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    good=0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,val):
            if not node: return 
            if node.val>=val:
                self.good+=1
                val=node.val
            dfs(node.left,val)
            dfs(node.right,val)
        dfs(root,root.val)
        return self.good
