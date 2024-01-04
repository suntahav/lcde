from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for k in c.keys():
            t = c[k]%3
            tum = c[k]//3
            if (t ==1 and tum ==0) :
                return -1
            if t!=0:
                res += (tum + 1)
            else:
                res += tum
        return res
        