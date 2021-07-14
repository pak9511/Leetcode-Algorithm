class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic=collections.defaultdict(list)
        for path in paths:
            tmp=path.split(' ')
            for t in tmp[1:]:
                dic[t.split('.txt')[1]].append(tmp[0]+'/'+t.split('.txt')[0]+'.txt')
        return [i for i in dic.values() if len(i)>1] 
