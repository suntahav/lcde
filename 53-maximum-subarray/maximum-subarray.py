class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        m = float("-inf")
        res = float("-inf")

        for n in nums:
            m = max(n, m+n)
            res = max(res, m)
        return res