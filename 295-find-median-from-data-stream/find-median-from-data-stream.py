import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)
        

    def addNum(self, num: int) -> None:
        if len(self.right) == 0 and len(self.left) == 0:
            heapq.heappush(self.right, num)
        else:
            if num >= self.right[0]:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -num)
        while abs(len(self.right) - len(self.left)) > 1:
            if len(self.right) > len(self.left):
                heapq.heappush(self.left, -heapq.heappop(self.right))
            else:
                heapq.heappush(self.right, -heapq.heappop(self.left))

            
            
            
            
        

    def findMedian(self) -> float:
        # print(self.l, self.small)
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            if len(self.left) > len(self.right):
                return -self.left[0]
            else:
                return self.right[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()