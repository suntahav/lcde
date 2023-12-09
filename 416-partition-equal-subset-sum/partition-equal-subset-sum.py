class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==0:
            target = sum(nums)//2
        else:
            return False
        
        t = [[0]*(target+1) for i in range(len(nums)+1)]
        t[0][0] = 1

        for i in range(1, len(nums)+1):
            for j in range(target+1):
                if nums[i-1] <= j:
                    t[i][j] = t[i-1][j] | t[i-1][j-nums[i-1]]
                else:
                    t[i][j] = t[i-1][j]
        return t[len(nums)][target] == 1
        