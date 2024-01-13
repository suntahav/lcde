from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        LEN = len(s)
        s = Counter(s)
        t = Counter(t)
        overlap = 0
        for key in s.keys():
            if key in t:
                overlap += min(s[key], t[key])
        res = LEN - overlap
        return res
        