class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointer approach with moving left only if right num less than left
        lp = 0
        rp = 1
        max_profit = 0
        while rp < len(prices):
            if prices[rp] == prices[lp]:
                rp += 1
            elif prices[rp] < prices[lp]:
                lp = rp
                rp += 1
            else :
                if max_profit < (prices[rp] - prices[lp]):
                    max_profit = prices[rp] - prices[lp]
                rp += 1
            
            
        return max_profit    