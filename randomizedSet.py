import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.index = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.index)
        self.index.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            if len(self.index) > 1: #this isn't necessary but maybe speeds things up a small bit
                self.dict[self.index[-1]] = self.dict[val]
                self.index[self.dict[val]], self.index[-1] = self.index[-1], self.index[self.dict[val]]
            self.index.pop()
            del self.dict[val]
            return True
        return False
        
    def getRandom(self) -> int:
        random_num = random.randint(0, len(self.index) - 1)
        return self.index[random_num]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()