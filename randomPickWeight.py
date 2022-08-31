from random import randint

class Solution:
    #find the sum(w) to determine range of random values
    #create a list with local sums at each step of w
    #generate a random number from 1 to the sum(w)
    #if the random number is less than the local sum then return the index which should correspond to the picked index
    #time complexity O(n)
    #space complexity O(n)
    #this can be improved with binary search which I'll probably do next
    def __init__(self, w: List[int]):
        current_total = 0
        self.w_totals = []
        for num in w:
            current_total += num
            self.w_totals.append(current_total)
        self.total = current_total
    
    def pickIndex(self) -> int:
        random_num = randint(1, self.total)
        for index in range(0, len(self.w_totals)):
            if self.w_totals[index] >= random_num:
                return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()