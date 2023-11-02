class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        dp = {}
        MIN = min(coins)
        for c in coins:
            dp[c] = 1
        def calculate(amt):
            if amt == 0:
                dp[amt] = 0
                return dp[amt]
            if amt in dp:
                return dp[amt]
            if amt < MIN:
                dp[amt] = -1
                return dp[amt]
            else:
                for c in coins:
                    if c > amt:
                        continue
                    else:
                        remainder = amt - c
                        # print(remainder)
                        tot_coins = calculate(remainder)
                        if tot_coins != -1:
                            if amt in dp:
                                dp[amt] = min(1 + tot_coins, dp[amt]) 
                            else:
                                dp[amt] = 1 + tot_coins
                if amt in dp:
                    return dp[amt]
                else:
                    dp[amt] = -1
                    return dp[amt]
        
        total_coins = calculate(amount)
        return total_coins
