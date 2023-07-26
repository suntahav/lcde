class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        max_len = 0
        lp,rp = 0, 0

        while rp < len(s):
            if s[rp] in hash_set:
                while s[lp] != s[rp]:
                    hash_set.remove(s[lp])
                    lp += 1
                lp += 1
            hash_set.add(s[rp])
            rp += 1
            if max_len < len(hash_set):
                max_len = len(hash_set)
        return max_len
