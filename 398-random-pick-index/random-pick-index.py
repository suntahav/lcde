import random
class Solution:

    def __init__(self, nums: List[int]):
        self.mapper = {}
        for idx,num in enumerate(nums):
            if num in self.mapper:
                self.mapper[num].append(idx)
            else:
                self.mapper[num] = [idx]

    def pick(self, target: int) -> int:
        i = random.randint(0, len(self.mapper[target])-1)
        return self.mapper[target][i]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)