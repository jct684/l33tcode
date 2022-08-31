from random import randint

class Solution:
    #find the sum(w) to determine range of random values
    #create a list with local sums at each step of w
    #generate a random number from 1 to the sum(w)
    #if the random number is less than the local sum then return the index which should correspond to the picked index
    #time complexity O(n) for creating the local sums, O(log n) for searching it
    #space complexity O(n)
    def __init__(self, w: List[int]):
        current_total = 0
        self.w_totals = []
        for num in w:
            current_total += num
            self.w_totals.append(current_total)
        self.total = current_total
    
    def pickIndex(self) -> int:
        if len(self.w_totals) == 0:
            return 0
        else:
            random_num = randint(1, self.total)
            return modified_binary_search(self.w_totals, random_num)

def modified_binary_search(array, target):
    right = len(array) - 1
    left = 0
    while left < right:
        mid = left + (right - left) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            left = mid + 1
        else:
            right = mid
    return left
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()