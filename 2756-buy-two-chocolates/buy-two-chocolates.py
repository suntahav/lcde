class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        val = money - sum(sorted(prices)[:2])
        return val if val >= 0 else money
        