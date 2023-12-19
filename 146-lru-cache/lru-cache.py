from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.store = OrderedDict()
        self.c = capacity
        self.n = 0
        

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        else:
            res = self.store[key]
            self.store.pop(key)
            self.store[key] = res
            return res
        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.pop(key)
            self.store[key] = value
        else:
            if self.c == self.n:
                delete = next(iter(self.store))
                self.store.pop(delete)

                self.store[key] = value
            else:
                self.store[key] = value
                self.n += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)