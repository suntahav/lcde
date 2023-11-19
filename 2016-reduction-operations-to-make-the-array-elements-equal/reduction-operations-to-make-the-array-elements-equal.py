class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        LEN = len(nums)
        curr_num = nums[0]
        inc = 0
        for i in range(1, LEN):
            if curr_num != nums[i]:
                inc += 1
                res += inc
                curr_num = nums[i]
            else:
                res += inc
        return res


        