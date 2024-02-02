class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def createDigit(start, length):
            num = 0
            for i in range(length):
                num += (start + i) * 10**(length - i-1)
            return num
        all_nums = []
        for i in range(2, 10):
            for j in range(1, 11-i):
                all_nums.append(createDigit(j, i))
        res = []
        for num in all_nums:
            if num >= low and num <= high:
                res.append(num)
        return res

        