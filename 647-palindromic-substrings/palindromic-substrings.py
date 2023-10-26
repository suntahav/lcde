class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        res = []
        def expand(left, right):
            temp = []
            while left >=0 and right < length and s[left] == s[right]:
                res.append(s[left: right + 1])
                left -= 1
                right += 1
        
        for i in range(length):
            expand(i, i)
            expand(i, i+1)
        #handling the case where left != right(i != i+1)
        # res.remove('')
        
        return len(res)
        