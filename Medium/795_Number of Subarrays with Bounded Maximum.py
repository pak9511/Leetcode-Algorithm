class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        count, start, end = 0, -1, -1
        
        for i in range(len(nums)):
            cur = nums[i]
            
            if cur>= left and cur <= right:
                end = i
            elif cur> right:
                start = i
                end = i
                
            count += (end - start)
            
        return count 
