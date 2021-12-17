class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=collections.Counter(s)
        most=count.most_common(1)[0][1]
        
        return all([i==most for i in count.values()])
