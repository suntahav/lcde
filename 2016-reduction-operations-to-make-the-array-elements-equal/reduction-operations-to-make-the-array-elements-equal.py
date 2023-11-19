class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        LEN = len(nums)
        curr_num = nums[0]
        inc = 0
        for num in nums:
            if curr_num != num:
                inc += 1
                curr_num = num
            res += inc
        return res


        