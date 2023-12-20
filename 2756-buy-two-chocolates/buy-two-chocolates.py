import heapq
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)
        a = heapq.heappop(prices)
        a += heapq.heappop(prices)
        val = money - a
        return val if val >= 0 else money
        