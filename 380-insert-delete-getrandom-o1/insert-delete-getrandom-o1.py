import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.map_idx:
            return False
        self.arr.append(val)
        self.map_idx[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val in self.map_idx:
            idx = self.map_idx[val]
            self.arr[idx] = self.arr[-1]
            self.map_idx[self.arr[-1]] = idx
            self.arr.pop()
            del self.map_idx[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()