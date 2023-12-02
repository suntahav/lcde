class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = [0] * len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums)):
            res[i] = max(nums[i], nums[i]+res[i-1])
        return max(res)
        