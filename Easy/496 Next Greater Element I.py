class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer=[]
        for idx_num,num in enumerate(nums1):
            idx=nums2.index(num)
            if idx==len(nums2)-1:
                answer.append(-1)
            else :
                for i in nums2[idx+1:]:
                    if i>num:
                        answer.append(i)
                        break
                if len(answer)-1!=idx_num:
                    answer.append(-1)
                
        return answer
