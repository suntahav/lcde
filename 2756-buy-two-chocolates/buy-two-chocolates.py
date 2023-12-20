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
        if val >= 0:
            return val
        return money
        