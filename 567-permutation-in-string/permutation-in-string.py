from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = Counter(s1)
        i = 0
        # left = 0
        LEN = len(s1)
        LEN2 = len(s2)
        while i<LEN2:
            if s2[i] in s:
                if i+LEN-1 >= LEN2:
                    break
                else:
                    t = Counter(s2[i:i+LEN])
                    # print(t)
                    # print(s)
                    if t == s:
                        return True
                    else:
                        i += 1
            else:
                i+=1
        return False
        