class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

        
class LRUCache:
    #use a dictionary to store nodes/objects associated with a key
    #use a doubly linked list over a singly linked list because deletions are O(1) in a doubly-linked list as opposed to O(n) time complexity
    #deletion and insertion O(1), retrieval is O(1) from cache
    #space complexity is O(capacity)
    def __init__(self, capacity: int):
        self.max_size = capacity
        self.size = 0
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        temp_1 = node.next
        temp_2 = node.prev
        node.prev.next = temp_1
        node.next.prev = temp_2
        self.size -= 1
    
    def add_after_head(self,node):
        temp_1 = self.head.next
        self.head.next = node
        node.next = temp_1
        node.prev = self.head
        node.next.prev = node
        self.size += 1
        
    def remove_before_tail(self):
        self.remove(self.tail.prev)
        
    def get(self, key: int) -> int:
        if key in self.cache:
            temp = self.cache.get(key)
            self.remove(self.cache.get(key))
            self.add_after_head(temp)
            return self.cache.get(key).value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache.get(key))
            self.cache.update({key: Node(key, value)})
            self.add_after_head(self.cache.get(key))
        else:
            self.cache.update({key: Node(key, value)})
            self.add_after_head(self.cache.get(key))
            if self.size > self.max_size:
                del self.cache[self.tail.prev.key]
                self.remove_before_tail()
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)