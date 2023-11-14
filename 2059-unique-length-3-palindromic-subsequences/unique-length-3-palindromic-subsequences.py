class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mapper = {}

        # unq_chars = set(s)
        LEN = len(s)
        # for c in unq_chars:
        #     start_idx = s.index(c)
        #     counter = 0
        #     last_idx = start_idx
        #     temp = set()
        #     for i in range(start_idx+1, LEN):
        #         if s[i] == c:
        #             if c not in temp and last_idx != start_idx:
        #                 temp.add(c)
        #             mapper[c] = len(temp)
        #             last_idx = i
        #         else:
        #             temp.add(s[i])
        # return sum((mapper.values()))
        for i,c in enumerate(s):
            if c in mapper:
                mapper[c].append(i)
            else:
                mapper[c] = [i]
        res = 0
        for c in mapper.keys():
            if len(mapper[c]) < 2:
                continue
            else:
                res += len(set(s[mapper[c][0]+1 : mapper[c][-1]]))
        return res
