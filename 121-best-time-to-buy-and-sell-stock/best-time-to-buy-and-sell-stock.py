class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lp = 0
        rp = 1
        max_profit = [0]
        while rp < len(prices):
            if prices[rp] == prices[lp]:
                rp += 1
            elif prices[rp] < prices[lp]:
                lp = rp
                rp += 1
            else :
                max_profit.append(prices[rp] - prices[lp])
                rp += 1
            
            
        return max(max_profit)    