class Solution:
    def countBits(self, n: int) -> List[int]:
        def get_bits(num):
            return bin(num)[2:].count('1')
        
        res = [0] * (n+1)
        for i in range(n+1):
            res[i] = get_bits(i)
        return res
        