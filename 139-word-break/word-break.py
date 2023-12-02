class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        mapper = {}
        for w in wordDict:
            if w[0] in mapper:
                mapper[w[0]].append(w)
            else:
                mapper[w[0]] = [w]
        
        def calculate(s):
            if s == "":
                return True
            if s in dp:
                return dp[s]
            start = s[0]
            if start not in mapper:
                dp[s] = False
                return dp[s]
            flag = False
            for word in mapper[start]:
                if s[:len(word)] == word:
                    if len(word) == len(s):
                        dp[s] = True
                        return dp[s]
                    elif len(word) > len(s):
                        continue
                    else:
                        flag = flag | calculate(s[len(word):])
                        if flag:
                            break
            dp[s] = flag
            return dp[s]
        return calculate(s)


        