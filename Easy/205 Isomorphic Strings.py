class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s,mapping_t = {},{}
        new_s,new_t = [],[]
        
        for c1,c2 in zip(s,t):
            # 문자열 s 변형
            if c1 not in mapping_s:
                mapping_s[c1] = s.index(c1)
                
            new_s.append(str(mapping_s[c1]))
            # 문자열 t 변형
            if c2 not in mapping_t:
                mapping_t[c2]=t.index(c2)
            new_t.append(str(mapping_t[c2]))
    
        return new_s == new_t
