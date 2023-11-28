class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        LEN  = len(nums)
        left = [0] * LEN
        left[0] = 1
        right = [0] * LEN
        right[LEN-1] = 1
        res =[0]*LEN
        for i in range(1, LEN):
            left[i] = left[i-1] * nums[i-1]
            right[LEN-1-i] = right[LEN-i] * nums[LEN-i]
        
        for i in range(LEN):
            res[i] = left[i] * right[i]
        return res
        