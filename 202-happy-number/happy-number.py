class Solution:
    def isHappy(self, n: int) -> bool:
        def get_squared(a):
            arr = list(str(a))
            arr = map(int, arr)
            # print(arr)
            func = lambda x : x**2
            arr = map(func, arr)
            return sum(arr)
        mapper = set()
        while True:
            
            if n == 1:
                return True
            if n in mapper:
                return False
            mapper.add(n)
            n = get_squared(n)

        