class Solution:
    def hammingWeight(self, n: int) -> int:
        mapper = lambda x : int(x)
        binary = str(bin(n))[2:]
        # print(binary)
        bin_list = list(binary)
        # print(bin_list)
        res = sum(map(mapper, bin_list))
        return res
        
        