class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        back_sum = [0]*LEN
        front_sum = [0] * LEN
        back_sum[LEN-1] = nums[LEN-1]
        front_sum[0] = nums[0]
        for i in range(1, LEN):
            front_sum[i] = front_sum[i-1] + nums[i]
            back_sum[LEN-i-1] = back_sum[LEN-i] + nums[LEN-i-1]
        res = []
        print(front_sum)
        print(back_sum)
        for i in range(LEN):
            temp = 0
            back = back_sum[i] - nums[i]
            front = front_sum[i] - nums[i]
            left = i
            right = LEN - i -1
            if front != 0:
                temp += nums[i] * left - front
            if back != 0:
                temp += back - nums[i] * right
            res.append(temp)
        
        return res
        