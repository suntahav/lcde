class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        dp = {}
        MIN = min(coins)
        for c in coins:
            dp[c] = (1, True)
        def calculate(amt):
            if amt == 0:
                dp[amt] = (0, True)
                return dp[amt]
            if amt in dp:
                return dp[amt]
            if amt < MIN:
                dp[amt] = (-1, False)
                return dp[amt]
            else:
                for c in coins:
                    if c > amt:
                        continue
                    else:
                        remainder = amt - c
                        # print(remainder)
                        tot_coins, is_Possible = calculate(remainder)
                        if is_Possible:
                            if amt in dp:
                                dp[amt] = (min(1 + tot_coins, dp[amt][0]), True)    
                            else:
                                dp[amt] = (1 + tot_coins, True)
                if amt in dp:
                    return dp[amt]
                else:
                    dp[amt] = (-1, False)
                    return dp[amt]
        
        total_coins, is_Possible = calculate(amount)
        return total_coins
