class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        sorted_time = [x/y for x,y in zip(dist, speed)]
        sorted_time.sort()
        counter= 0
        l = len(sorted_time)
        for i in range(l):
            if sorted_time[i] - counter <= 0:
                break
            counter += 1

        return counter
        