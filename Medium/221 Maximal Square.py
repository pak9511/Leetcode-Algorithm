class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def check(x,y,length):
            if x+1<n and y+1<m and matrix[x+1][y+1]=='1':
            
                for l in range(length):
                    if matrix[x+1][y-l] != '1' or matrix[x-l][y+1] != '1':
                        return length
            else: return length
            
            return check(x+1,y+1,length+1)
        
        n,m=len(matrix),len(matrix[0])
        res=0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='1':
                    res=max(res,check(i,j,1))
        
        return res*res
