class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = nums[0]
        LEN = len(nums)
        for i in range(LEN):
            
            temp = nums[i]
            if temp > cache:
                cache = temp
            if (cache==0 and i < LEN-1) or cache < 0:
                return False
            if i + cache >= LEN-1:
                return True
            cache -= 1
        return True

        