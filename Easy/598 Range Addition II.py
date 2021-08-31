class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        
        xmin = sorted(ops,key=lambda x: x[0])[0][0]
        ymin = sorted(ops,key=lambda x: x[1])[0][1]
        return xmin*ymin
