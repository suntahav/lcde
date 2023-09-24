class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [-1] * len(nums)
        
        mem[0] = nums[0]
        if len(nums) >= 2:
            mem[1] = max(mem[0], nums[1])
        
        def dp(idx):
            #first two values of memoized are available from prior calculation
            if idx == 0:
                return mem[0]
            elif idx == 1:
                return mem[1]
            elif mem[idx] != -1:
                #return Memoized values
                return mem[idx]
            else:
                #run dp from end to back and store the results
                res = max(nums[idx]+dp(idx-2), dp(idx-1))
                mem[idx] = res
                return res
        #we are going from end to first so call at end
        return dp(len(nums)-1)