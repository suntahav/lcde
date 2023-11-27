class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def lcs(left, right, text1, text2):
            if len(text1) == left or len(text2) == right:
                return 0
            if (left,right) in dp:
                return dp[(left,right)]
            if text1[left] == text2[right]:
                dp[(left,right)] = 1 + lcs(left+1, right+1, text1, text2)
                return dp[(left,right)]
            dp[(left,right)] = max(lcs(left+1, right, text1, text2), lcs(left, right+1, text1, text2))
            return dp[(left,right)]
        return lcs(0, 0, text1, text2)
        