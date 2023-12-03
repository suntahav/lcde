class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        max_elem = max(intervals[-1][1], newInterval[1])
        arr = [0] * (max_elem+2)
        for i in range(len(intervals)):
            for j in range(intervals[i][0], intervals[i][1]+1):
                if arr[j] == 1:
                    continue
                if j == intervals[i][0] and j > 0 and arr[j-1] == 1:
                        arr[j-1] = 2
                arr[j] = 1
        # print(arr)
        for j in range(newInterval[0], newInterval[1]+1):
            if arr[j] == 1:
                    continue
            if j == newInterval[1] and arr[j+1] == 1:
                    arr[j] = 2
            elif j == newInterval[0] and arr[j-1] == 1:
                if arr[j] != 2:
                    arr[j-1] = 2
                arr[j] = 1
            else:
                arr[j] = 1
        # print(arr)
        res = []
        start = -1
        for i in range(max_elem+2):
            if start == -1 and arr[i]>=1:
                start = i
            if start > -1 and arr[i] == 0:
                res.append([start, i-1])
                start = -1
            if start > -1 and arr[i] == 2:
                res.append([start, i])
                start = -1
        # print(arr)
        return res
            


        