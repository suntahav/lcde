from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        c = Counter(nums)
        max_val = c[max(c, key=c.get)]
        res = [[]for i in range(max_val)]
        for k in c.keys():
            for i in range(c[k]):
                res[i].append(k)
        
        return res
        