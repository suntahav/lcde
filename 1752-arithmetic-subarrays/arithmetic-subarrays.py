from collections import Counter
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for start, end in zip(l,r):
            temp = nums[start:end+1]
            if len(temp) < 2:
                res.append(False)
                continue
            temp.sort()
            diff = temp[1]-temp[0]
            temp_res = True
            for i in range(1, len(temp)):
                if temp[i] - temp[i-1] != diff:
                    temp_res = False
                    break
            res.append(temp_res)
        return res


        