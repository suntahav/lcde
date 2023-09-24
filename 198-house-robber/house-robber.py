class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [-1] * len(nums)
        
        mem[0] = nums[0]
        if len(nums) >= 2:
            mem[1] = max(mem[0], nums[1])
        
        def dp(idx):
            if idx == 0:
                return mem[0]
            elif idx == 1:
                return mem[1]
            elif mem[idx] != -1:
                return mem[idx]
            else:
                res = max(nums[idx]+dp(idx-2), dp(idx-1))
                mem[idx] = res
                return res
        
        return dp(len(nums)-1)