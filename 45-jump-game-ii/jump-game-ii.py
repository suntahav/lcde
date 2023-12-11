class Solution:
    def jump(self, nums: List[int]) -> int:
        LEN = len(nums)
        res = [10000000] * LEN

        res[LEN-1] = 0
        i= LEN-2
        while i >=0:
            min_val = 10000000
            for j in range(1, nums[i]+1):
                if i+j < LEN:
                    res[i] = min(res[i], 1+res[i+j])
            i -= 1
        return res[0]

        