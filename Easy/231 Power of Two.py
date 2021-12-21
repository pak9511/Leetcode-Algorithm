class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if 0<=n<2: return n
        if n<0 : return False
        log=math.log2(n)
        
        if int(log)==log: return True
        else: return False
