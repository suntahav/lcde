class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        LEN = len(nums)
        max_val = -1
        for i in range(LEN//2):
            if max_val < nums[i] + nums[LEN - 1 -i]:
                max_val = nums[i] + nums[LEN - 1 -i]
        return max_val

        