class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        else:
            isIncreasing = False
            isDecreasing = False
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    isIncreasing = True
                elif nums[i] < nums[i-1]:
                    isDecreasing = True
            if isDecreasing:
                #decreasing
                for i in range(1, len(nums)):
                    if nums[i] > nums[i-1]:
                        return False
                return True
            elif isIncreasing:
                for i in range(1, len(nums)):
                    if nums[i] < nums[i-1]:
                        return False
                return True
            else:
                return True
        