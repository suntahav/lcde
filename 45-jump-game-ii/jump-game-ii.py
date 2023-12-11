class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [-1] * len(nums)

        def calculate(idx):
            if idx == len(nums)-1:
                return 0
            if res[idx] != -1:
                return res[idx]
            min_val = 1000000
            for i in range(1, nums[idx]+1):
                if idx + i >= len(nums):
                    continue
                min_val = min(min_val, 1+calculate(idx+i))
            res[idx] = min_val
            return min_val
        return calculate(0)

        