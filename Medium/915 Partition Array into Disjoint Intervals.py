class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        nums=collections.deque(nums)
        left,l_max=0, nums.popleft()
        r_min=min(nums)
        
        while True:
            if l_max > r_min:
                left+=1
                tmp=nums.popleft()
                if tmp==r_min:
                    r_min=min(nums)
                elif tmp >l_max:
                    l_max=tmp
                
            elif l_max <=r_min:
                return left+1
