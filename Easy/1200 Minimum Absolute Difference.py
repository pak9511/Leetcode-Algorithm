class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff=sys.maxsize
        
        for i in range(len(arr)-1):
            cur=abs(arr[i+1]-arr[i])
            if cur<diff:
                diff,res=cur, [[arr[i],arr[i+1]]]
            elif cur==diff:
                res.append([arr[i],arr[i+1]])
        return res
