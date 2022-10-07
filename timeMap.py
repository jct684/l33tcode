from collections import defaultdict

class TimeMap:

    def __init__(self):
        #dictionary using key to provide an index
        #dictionary where the key is an index and corresponding value is returned
        #check dictionary to determine indices corresponding to key
        #using the value closest to the current value return value stored in index (linear search)
        #this could be improved with a modified binary search with search space 2 but I'm too lazy
        #Note: all timestamps are strictly increasing so no need to sort
        self.index_dict = defaultdict(lambda :[])
        self.timestamp_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp_dict[timestamp] = value
        self.index_dict[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if (self.index_dict[key] == []):
           return ""
        else:
            hi = len(self.index_dict[key]) - 1
            while (self.index_dict[key][hi] > timestamp):
                hi -= 1
                if (hi == -1):
                    return ""
            return self.timestamp_dict[self.index_dict[key][hi]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)