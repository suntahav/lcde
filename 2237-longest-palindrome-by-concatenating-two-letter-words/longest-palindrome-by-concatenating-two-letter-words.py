class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mapper = {}
        for w in words:
            if w in mapper:
                mapper[w] += 1
            else:
                mapper[w] = 1
        l = 0
        flag = False
        for w in words:
            if w[0] == w[1]:
                if w in mapper:
                    if mapper[w] % 2 == 0:
                        l += 2 * mapper[w]
                        del mapper[w]
                    else:
                        if mapper[w] == 1 and not flag:
                            l += 2
                            flag = True
                        else:
                            if not flag:
                                flag = True
                                l += 2* (mapper[w])
                            else:
                                l += 2* (mapper[w] - 1)
                        del mapper[w]
                continue
            if w in mapper:
                if w[::-1] in mapper:
                    mapper[w] -= 1
                    mapper[w[::-1]] -= 1
                    if mapper[w] == 0:
                        del mapper[w]
                    if mapper[w[::-1]] == 0:
                        del mapper[w[::-1]]
                    l += 4
        return l

        