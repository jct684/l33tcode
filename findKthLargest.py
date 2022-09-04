import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #create heap using an array of size k
        #add to heap until reach k, then add to heap and pop from heap until only largest k elements remain
        #the smallest of the k elements is the answer
        #time complexity O(n log(k))
        #space complexity O(t)
        return heapq.nlargest(k, nums)[-1]