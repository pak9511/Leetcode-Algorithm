class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd, even=[],[]
        
        for num in nums:
            if num%2==0:
                even.append(num)
            else: odd.append(num)
                
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=even.pop()
            else:
                nums[i]=odd.pop()
        
        return nums
