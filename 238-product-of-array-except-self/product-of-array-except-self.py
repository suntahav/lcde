class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        LEN  = len(nums)
        left = 1
        right = 1
        counter_zero = 0
        for i in range(LEN):
            right *= nums[i]
            if nums[i] == 0:
                counter_zero += 1
        res = [0] * LEN
        i = 0
        while i < LEN:
            
            if nums[i] != 0:
                right = right // nums[i]
            else:
                counter_zero -= 1
                if counter_zero == 0:
                    right = 1
                    for j in range(i+1, LEN):
                        right *= nums[j]
            if left==0 or right==0:
                res[i] = 0
            res[i] = left * right
            left *= nums[i]
            i+=1
        return res
        