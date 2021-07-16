class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans=0

        for left in range(len(nums)-2):
            right=left+2
            if nums[left]==0:continue
                
            for mid in range(left+1,len(nums)-1):
                while right<len(nums) and nums[left]+nums[mid]> nums[right]:
                    right+=1
                ans+=right-mid-1
                
        return ans
