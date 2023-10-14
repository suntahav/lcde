class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = [0]
        l = len(nums)
        cache = {}
        # @lru_cache(None)
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
                if (idx+1, sum+nums[idx]) in cache:
                    a = cache[(idx+1, sum+nums[idx])]
                else:
                    a = recCall(idx + 1, sum+nums[idx])
                    cache[(idx+1, sum+nums[idx])] = a
                if (idx + 1, sum-nums[idx]) in cache:
                    b = cache[(idx + 1, sum-nums[idx])]
                else:
                    b = recCall(idx + 1, sum-nums[idx])
                    cache[(idx + 1, sum-nums[idx])] = b
                return  a + b
                #Remove
                
        return recCall(0, 0)
        # return res[0]
        