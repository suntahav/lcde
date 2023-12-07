class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = collections.defaultdict(list)
        for i, num in enumerate(numbers):
            d[num].append(i)
        
        for i in range(len(numbers)):
            n_t = target - numbers[i]
            if n_t == numbers[i]:
                if len(d[n_t]) > 1:
                    return [d[n_t][0]+1, d[n_t][1]+1]
            if n_t in d:
                return [i+1, d[n_t][0]+1]
        