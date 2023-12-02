class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        LEN = len(nums)
        m = nums[0]
        res = max(nums)
        for i in range(1, LEN):
            m = max(nums[i], nums[i]+m)
            res = max(res, m)
        return res
        