class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort()
        new_piles = piles[n:]
        return sum([new_piles[i] for i in range(0, len(new_piles), 2)])

        