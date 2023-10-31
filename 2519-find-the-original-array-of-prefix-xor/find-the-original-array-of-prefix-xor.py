class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        res.append(pref[0])
        xor_cum = pref[0]
        for i in range(1, len(pref)):
            val = xor_cum ^ pref[i]
            res.append(val)
            xor_cum = val ^ xor_cum
        return res
        