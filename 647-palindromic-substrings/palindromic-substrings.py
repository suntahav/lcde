class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        res = []
        def expand(left, right):
            temp = []
            while left >=0 and right < length and s[left] == s[right]:
                temp.append(s[left: right + 1])
                left -= 1
                right += 1
            return temp
        
        for i in range(length):
            a = expand(i, i)
            b = expand(i, i+1)
            res.extend(a)
            res.extend(b)
        #handling the case where left != right(i != i+1)
        # res.remove('')
        
        return len(res)
        