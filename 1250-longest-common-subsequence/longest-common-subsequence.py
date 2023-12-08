class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def lcs(left, right):
            if left == -1 or right == -1:
                return 0
            if (left,right) in dp:
                return dp[(left,right)]
            if text1[left] == text2[right]:
                dp[(left,right)] = 1 + lcs(left-1, right-1)
                return dp[(left,right)]
            dp[(left,right)] = max(lcs(left-1, right), lcs(left, right-1))
            return dp[(left,right)]
        return lcs(len(text1)-1, len(text2)-1)
        