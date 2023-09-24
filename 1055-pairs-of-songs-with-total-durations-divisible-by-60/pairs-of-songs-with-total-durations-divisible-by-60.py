class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mapper = {}
        for t in time:
            if t%60 in mapper:
                mapper[t%60] += 1
            else:
                mapper[t%60] = 1
        res = 0
        for t in time:
            mod = t%60
            mod_reqd = (60 - mod)%60
            if mod == mod_reqd:
                res += (mapper[mod] -1)
            else:
                if mod_reqd in mapper:
                    res += mapper[mod_reqd]
        return res//2
            
        