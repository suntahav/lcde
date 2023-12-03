class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = sorted(intervals, key= lambda x:x[0])
        res = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i][0] <= res[-1][1]:
                if res[-1][1] <= arr[i][1]:
                    res[-1][1] = arr[i][1]
                else:
                    continue
            else:
                res.append(arr[i])
        return res
                    
