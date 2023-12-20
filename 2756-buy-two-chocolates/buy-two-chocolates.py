import heapq
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        f,s = 101,101
        for p in prices:
            if p < f:
                s = f
                f = p
            elif p<s:
                s=p
        val = money -f-s
        return val if val >= 0 else money
        