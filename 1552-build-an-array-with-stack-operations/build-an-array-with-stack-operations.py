class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 1
        h_map = {}
        for j in range(len(target)):
            h_map[target[j]] = 1
        MAX = max(target)
        res = []
        while i <= MAX:
            res.append("Push")
            if i not in h_map:
                res.append("Pop")
            i+= 1
        return res
        