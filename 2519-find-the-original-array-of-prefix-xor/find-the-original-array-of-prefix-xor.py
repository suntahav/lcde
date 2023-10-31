class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [0] * len(pref)
        res[0] = pref[0]
        xor_cum = pref[0]
        for i in range(1, len(pref)):
            res[i] = xor_cum ^ pref[i]
            xor_cum = res[i] ^ xor_cum
        return res
        