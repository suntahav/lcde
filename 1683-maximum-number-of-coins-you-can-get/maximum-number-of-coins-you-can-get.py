class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort()
        return sum([piles[i + n] for i in range(0, 2*n, 2)])

        