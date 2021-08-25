class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        A=re.sub('[^0-9-]'," ",num1).split()
        B=re.sub('[^0-9-]'," ",num2).split()
 
        return str(eval(A[0]+'*'+B[0]+'-'+A[1]+'*'+B[1]))+'+'+\
               str(eval(A[0]+'*'+B[1]+'+'+A[1]+'*'+B[0]))+'i'
