class Solution(object):
    def longestOnes(self, nums, k):
        if nums.count(0)<=k:
            return len(nums)
        
        ans=0
        left,right=0,k
        count=nums[left:right].count(0)  
        
        while left<len(nums) and right<=len(nums):
            if count<k:
                right+=1
                if nums[right-1]==0:
                    count+=1
            
            elif count==k:
                ans=max(ans, right-left)
                right+=1
                if right<=len(nums) and nums[right-1]==0:
                    count+=1
                
            else:
                left+=1
                if nums[left-1]==0:
                    count-=1
                
        return ans
