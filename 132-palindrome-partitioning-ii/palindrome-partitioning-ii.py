class Solution:
    
    def minCut(self, string: str) -> int:
        n=len(string)
        t = [[-1 for i in range(n+2)]for j in range(n+2)]
        # @cache
        def isPalin(s):
            return s == s[::-1]
        # @cache   
        def solve(i, j):
            if i >= j:
                return 0
            if t[i][j] != -1:
                return t[i][j]
            if isPalin(string[i:j+1]):
                t[i][j] = 0
                return 0
            min_cut = 1e9
            for k in range(i, j):
                if isPalin(string[i:k+1]):
                   temp =solve(k+1,j)+1
                min_cut = min(min_cut, temp)
            t[i][j] = min_cut
            return min_cut
        
        return solve(0, len(string)-1) 