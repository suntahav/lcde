class Solution:
    def rob(self, nums: List[int]) -> int:
        mem1 = [-1] * (len(nums)-1)
        mem2 = [-1] * (len(nums)-1)
        num = nums[:len(nums)-1]

        if len(nums) <= 2:
            return max(nums)
        #initialize the base case for memoize if first is included
        mem1[0] = nums[0]
        mem1[1] = max(nums[0], nums[1])
        #initialize the base case for memoize if first is not included
        mem2[0] = nums[1]
        mem2[1] = max(nums[1], nums[2])

        def dp(idx, num):
            if idx == 0:
                mem[0] = num[0]
                return mem[0]
            elif idx == 1:
                mem[1] = max(mem[0], num[1])
                return mem[1]
            elif mem[idx] != -1:
                return mem[idx]
            else:
                res = max(num[idx]+dp(idx-2, num), dp(idx-1, num))
                mem[idx] = res
                return res
        
        mem = mem1
        include_res = dp(len(num)-1, num)
        mem = mem2
        num = nums[1:]
        exclude_res = dp(len(num)-1, num)
        print(mem1, mem2)
        return max(exclude_res, include_res)
        