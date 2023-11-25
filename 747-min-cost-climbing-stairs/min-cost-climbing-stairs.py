class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        def calculate(idx, cost):
            #if already exist
            if dp[idx] != -1:
                return dp[idx]
            #base case
            if idx == len(cost)-1:
                dp[idx] = cost[-1]
                return cost[-1]
            
            if idx == len(cost)-2:
                dp[idx] = cost[-2]
                return cost[-2]
            dp[idx] = cost[idx] + min(calculate(idx+1, cost), calculate(idx+2, cost))
            return  dp[idx]
        
        return min(calculate(0, cost), calculate(1, cost))
        