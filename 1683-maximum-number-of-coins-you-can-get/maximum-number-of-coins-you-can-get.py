class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort()
        res = 0
        for i in range(0, 2*n, 2):
            res += piles[i + n]
        return res

        