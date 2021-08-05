# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        def dfs(node,path,target):
            if not node: return
            path.append(node.val)
            target-=node.val
            if node.left ==None and node.right==None:
                if target==0:
                    ans.append(path[:])
            else:
                dfs(node.left,path,target)
                dfs(node.right,path,target)
            path.pop()

        ans=[]
        dfs(root,[],targetSum)
        return ans
