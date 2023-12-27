class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        s = 0
        m = -1
        lc = ''
        res = 0
        counter = 0
        for idx,c in enumerate(colors):
            if lc == '':
                lc = c
                s += neededTime[idx]
                m = max(m, neededTime[idx])
                counter = 1
            elif lc == c:
                s += neededTime[idx]
                m = max(m, neededTime[idx])
                counter += 1
            else:
                lc = c
                res += (s - m)
                m = neededTime[idx]
                s = neededTime[idx]
                counter = 1
        if counter > 1:
            res += (s-m)
        return res

        