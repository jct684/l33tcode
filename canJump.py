class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #input: array of integers
        #output: true or false (last index or not)
        #test 1: [2, 3, 1, 1, 4], True
        #test 2: [3, 2, 1, 0, 4], False
        #test 3: [3, 2, 1, 2, 4], True
        #time complexity O(n)
        #space complexity O(1)
        if len(nums)<2:
            return True
        end = len(nums)-1
        curr = len(nums)-2
        while end > 0 and curr >= 0:
            if nums[curr] >= end - curr:
                end = curr
            curr -= 1
        return end == 0