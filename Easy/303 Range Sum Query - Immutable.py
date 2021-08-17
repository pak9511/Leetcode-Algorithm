class NumArray:
    def __init__(self, nums):
        self.arr = list(accumulate(nums))

    def sumRange(self, left, right):
        if left==0:
            return self.arr[right]
        else:
            return self.arr[right]-self.arr[left-1]
          
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
