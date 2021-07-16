class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=list(set(nums))
        nums.sort()
        length,max_length=0,0
        
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                length+=1
            else:
                length=0
            max_length=max(max_length,length)
        return max_length+1
