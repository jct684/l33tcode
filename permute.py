class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #time complexity O(n! * n)
        #space complexity O(n)
        res = []
        def backtrack(candidate):
            #output solution
            if len(nums) == len(candidate):
                res.append(candidate.copy())
                return
            #explore all candidates
            for num in nums:
                #check candidate validity
                if num not in candidate:
                    candidate.append(num)
                    #backtrack
                    backtrack(candidate)
                    #remove
                    candidate.pop()
        backtrack([])
        return res