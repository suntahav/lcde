class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [0] * len(nums)
        mem[0] = nums[0]
        if len(nums) >= 2:
            mem[1] = max(mem[0], nums[1])
        else:
            return mem[0]
        for i in range(2, len(nums)):
            mem[i] = max(mem[i-1] , mem[i-2] + nums[i])
        
        return max(mem)
        