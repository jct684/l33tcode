class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #time complexity O(n*2^n)
        #space complexity O(n)
        nums.sort()
        res = []
        
        def backtrack(candidate, start):
            res.append(candidate[:])
            for i in range(start, len(nums)):
                if i!=start and nums[i] == nums[i-1]:
                    continue
                candidate.append(nums[i])
                backtrack(candidate, i+1)
                candidate.pop()
        
        backtrack([], 0)
        return res