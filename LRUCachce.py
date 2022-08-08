class LRUCache:
    #Looks like I could just add attributes as keys with associated values
    #I could then use an array to check order of use/access to determine which to delete
    #Maybe to speed this up I can try a doubly linked list instead of an array next

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.size = 0
        self.last_used = []

    def get(self, key: int) -> int:
        if hasattr(self, f"{key}"):
            self.last_used.append(key)
            self.last_used.remove(key)
            return getattr(self, f'{key}')
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if hasattr(self, f"{key}"):
            setattr(self, f'{key}', value)
            self.last_used.append(key)
            self.last_used.remove(key)
        else:
            setattr(self, f'{key}', value)
            self.size += 1
            self.last_used.append(key)
            if self.size > self.max_size:
                self.size -= 1
                delattr(self, f'{self.last_used.pop(0)}')


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)