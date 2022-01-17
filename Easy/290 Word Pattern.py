class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionary,words={},s.split()
        
        if len(pattern) != len(s.split()): return False
        if len(set(pattern)) != len(set(s.split())): return False
        
        for i in range(len(words)):
            if words[i] not in dictionary:
                dictionary[words[i]]=pattern[i]
            elif dictionary[words[i]] !=pattern[i]: return False
        return True
