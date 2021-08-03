class Solution(object):
    def subsetsWithDup(self, nums):
        res=[]
        
        def dfs(ele,start):
            if sorted(ele) not in res:
                res.append(sorted(ele[:]))
            for i in range(start,len(nums)):
                ele.append(nums[i])
                dfs(ele,i+1)
                ele.pop()
        dfs([],0)
        return res
