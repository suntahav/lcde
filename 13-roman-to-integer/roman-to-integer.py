class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        mapper = {
            'I':1,
            'V': 5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res = 0
        prev = s[0]
        res += mapper[prev]
        for i in range(1, len(s)):
            if mapper[prev] > mapper[s[i]]:
                res -= mapper[s[i]]
                prev = s[i]
            else:
                res += mapper[s[i]]
                prev = s[i]
        return res