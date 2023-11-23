from collections import Counter
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for start, end in zip(l,r):
            temp = nums[start:end+1]
            temp = sorted(temp)
            temp = [temp[i]-temp[i-1] for i in range(1, len(temp))]
            if max(temp) == min(temp):
                res.append(True)
            else:
                res.append(False)
        return res


        