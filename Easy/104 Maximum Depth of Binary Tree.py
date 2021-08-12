class Solution(object):
    ans=0
    def maxDepth(self, root):
        def dfs(node,depth):
            if not node:
                return self.ans
            if node.left:
                dfs(node.left,depth+1)
            if node.right:
                dfs(node.right,depth+1)
            else: 
                self.ans=max(self.ans,depth)
        dfs(root,1)
        return self.ans
