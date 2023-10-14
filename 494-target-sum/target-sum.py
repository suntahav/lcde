class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = [0]
        l = len(nums)
        @lru_cache(None)
        def recCall(idx, sum):
            #Base case
            if l == idx:
                if target == sum:
                    # if target == 0:
                    #     res[0] += 1
                    return 1
                else:
                    return 0
            else:
                #One for include
               return recCall(idx + 1, sum+nums[idx]) + recCall(idx + 1, sum-nums[idx])
                #Remove
                
        return recCall(0, 0)
        # return res[0]
        