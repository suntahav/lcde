class MinStack:

    def __init__(self):
        self.stack = []
        self.min_idx = -1
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_idx >= 0:
            if self.stack[self.min_idx] > val:
                self.min_idx = self.stack.index(val)
        else:
            self.min_idx = 0

    def pop(self) -> None:
        if self.min_idx == len(self.stack)-1:
            res = self.stack.pop()
            if self.stack:
                self.min_idx = self.stack.index(min(self.stack))
            else:
                self.min_idx = -1
            return res
        else:
            return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.min_idx]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()