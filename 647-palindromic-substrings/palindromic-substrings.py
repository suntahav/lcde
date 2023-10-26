class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        res = 0
        def expand(left, right):
            temp = []
            res = 0
            while left >=0 and right < length and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            return res
        
        for i in range(length):
            res += expand(i, i)
            res += expand(i, i+1)
        #handling the case where left != right(i != i+1)
        # res.remove('')
        
        return res
        