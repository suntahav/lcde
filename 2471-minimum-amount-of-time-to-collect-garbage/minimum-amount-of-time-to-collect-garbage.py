# from collections import Counter
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        paper_cache = 0
        glass_cache = 0
        metal_cache = 0
        LEN = len(garbage)
        res = 0
        for i in range(LEN):
            if i > 0:
                metal_cache += travel[i-1]
                paper_cache += travel[i-1]
                glass_cache += travel[i-1]

            if 'M' in garbage[i]:
                res += metal_cache
                metal_cache = 0
            
            if 'P' in garbage[i]:
                res += paper_cache
                paper_cache = 0
            
            if 'G' in garbage[i]:
                res += glass_cache
                glass_cache = 0
            
            res += len(garbage[i])
        return res
            




        