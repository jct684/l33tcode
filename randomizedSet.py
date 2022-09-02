import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.index = []
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.index.append(val)
        self.dict[val] = self.size
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            if len(self.index) > 1 and self.dict.get(val) != self.size - 1:
                temp = self.index.pop()
                self.index[self.dict.get(val)] = temp
                self.dict[temp] = self.dict.get(val)
            else:
                self.index.pop()
            del self.dict[val]
            self.size -= 1
            return True
        return False
        
    def getRandom(self) -> int:
        random_num = random.randint(0, self.size - 1)
        return self.index[random_num]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()