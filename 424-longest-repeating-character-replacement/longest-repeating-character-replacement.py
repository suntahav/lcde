class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = [0]*26
        lp,rp = 0, 0
        max_len = 0
        hash_map[ord(s[0]) - ord('A')] += 1
        changes = 0
        length = 1
        while rp < len(s)-1:
            #check  the max length
            if max_len < length:
                max_len = length

            # handle changes less than k
            if sum(hash_map) - max(hash_map) < k:
                rp += 1
                length += 1
                hash_map[ord(s[rp]) - ord('A')] += 1
            else:
                # max element
                rp += 1
                if hash_map[ord(s[rp]) - ord('A')] == max(hash_map):
                    length += 1
                    hash_map[ord(s[rp]) - ord('A')] += 1
                else:
                    rp -= 1
                    length -= 1
                    hash_map[ord(s[lp]) - ord('A')] -= 1
                    lp += 1
        
        if max_len < length:
            max_len = length   
        return max_len     

