class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [0] * len(pref)
        xor_cum = [0] * len(pref)
        res[0] = pref[0]
        xor_cum[0] = pref[0]
        for i in range(1, len(pref)):
            res[i] = xor_cum[i-1] ^ pref[i]
            xor_cum[i] = res[i] ^ xor_cum[i-1]
        return res
        