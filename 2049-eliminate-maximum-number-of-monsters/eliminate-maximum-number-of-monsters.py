class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_needed = [x/y for x,y in zip(dist, speed)]
        sorted_time = sorted(time_needed)
        buffer = 1
        counter= 0
        for i in range(len(sorted_time)):
            if sorted_time[i] - counter > 0:
                counter += 1
            else:
                break

        return counter
        