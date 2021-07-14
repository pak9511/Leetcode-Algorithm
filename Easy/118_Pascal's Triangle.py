class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp=[[1],[1,1]]
       
        if numRows<=2:
            return dp[:numRows]
        
        for i in range(2,numRows):
            x=len(dp[i-1])
            dp.append([1]+[dp[x-1][j]+dp[x-1][j-1] for j in range(1, i)]+[1])
            
        return dp
