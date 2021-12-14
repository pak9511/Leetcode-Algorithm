class Solution:
    def maxPower(self, s: str) -> int:
        if len(s)==2:
            return s.count(s[0])
        
        def expand(left, right):
            while right<len(s) and s[left]==s[right]:
                right+=1
            return right-left,right
        
        sub,i=1,0
        while i<len(s)-1:
            if s[i]==s[i+1]:
                cur,i=expand(i,i+1)
                sub=max(sub,cur)
            else: i+=1
        return sub
