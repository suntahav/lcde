class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr_max = ''
        length = len(s)
        #middle spread
        
        def expand(left, right):
            while left>=0 and right < length and s[left] == s[right] :
                left -= 1
                right += 1
            return s[left+1:right]
        
        for i in range(length):
            s_1 = expand(i,i)
            s_2 = expand(i,i+1)
            if len(s_1)>len(curr_max):
                curr_max = s_1
            if len(s_2)>len(curr_max):
                curr_max = s_2
        return curr_max
            
        