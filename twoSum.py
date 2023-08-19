class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #input: array of sorted integers
        #output: index + 1
        #test case: [-5, 0, 1, 4, 10], target = 4, answer = [2, 5]
        #two pointers on opposite ends, either increase low or decrease high based on target
        #O(n) time complexity
        #O(1) space complexity
        low = 0
        high = len(numbers)-1
        while(numbers[low] + numbers[high] != target):
            if target - numbers[low] < numbers[high]:
                high -= 1
            else:
                low += 1
        return [low+1, high+1]