class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) == 1:
            return 0
        
        prev = bank[0].count('1')
        LEN = len(bank)
        res = 0
        for i in range(1, LEN):
            if '1' in bank[i]:
                temp = bank[i].count('1')
                res += prev * temp
                prev = temp
        return res
        