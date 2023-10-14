class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
 
        l = len(nums)
        # cache = {}
        # # @lru_cache(None)
        # def recCall(idx, sum):
        #     #Base case
        #     if l == idx:
        #         if target == sum:
        #             # if target == 0:
        #             #     res[0] += 1
        #             return 1
        #         else:
        #             return 0
        #     else:
        #         #One for include
        #         if (idx+1, sum+nums[idx]) in cache:
        #             a = cache[(idx+1, sum+nums[idx])]
        #         else:
        #             a = recCall(idx + 1, sum+nums[idx])
        #             cache[(idx+1, sum+nums[idx])] = a
        #         if (idx + 1, sum-nums[idx]) in cache:
        #             b = cache[(idx + 1, sum-nums[idx])]
        #         else:
        #             b = recCall(idx + 1, sum-nums[idx])
        #             cache[(idx + 1, sum-nums[idx])] = b
        #         return  a + b
        #         #Remove
                
        # return recCall(0, 0)
        max_sum = sum(list(map(abs, nums)))
        if target > max_sum or target < -max_sum:
            return 0
        cache = [[0]* (l+1) for _ in range(max_sum*2 + 1)]
        cache[max_sum][0] = 1
        cache[max_sum - nums[0]][1] += 1
        cache[max_sum + nums[0]][1] += 1
        for col in range(2, len(cache[0])):
            for row in range(len(cache)):
                temp_sum = 0
                if row - nums[col-1] >=0:
                    temp_sum += cache[row - nums[col-1]][col-1]
                if row + nums[col-1] < len(cache):
                    temp_sum += cache[row + nums[col-1]][col-1]
                # if nums[col-1] == 0:
                #     temp_sum += cache[]
                cache[row][col] = temp_sum
                # if 
        
        if target >= 0:
            return cache[max_sum + target][len(cache[0])-1]
        else:
            return cache[max_sum - target][len(cache[0])-1]

                


        