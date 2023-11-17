class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        LEN = len(nums)
        new_arr_start = (nums[:LEN//2])[::-1]
        new_arr_end = nums[LEN//2:]
        res = [new_arr_start[i] + new_arr_end[i] for i in range(LEN//2)]
        return max(res)

        