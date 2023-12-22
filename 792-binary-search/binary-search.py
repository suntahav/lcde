class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def solve(left, right, target):
            if left==right:
                if nums[left]!=target:
                    return -1
                else:
                    return left
            
            if left > right:
                return -1
            
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return solve(left, mid-1, target)
            else:
                return solve(mid+1, right, target)
        
        return solve(0, len(nums)-1, target)