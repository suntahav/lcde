class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        for i in range(1, len(strs)):
            if min_len > len(strs[i]):min_len = len(strs[i])
        res = ''
        for i in range(min_len):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return res
            res += strs[0][i]
        return res