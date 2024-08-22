class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(candidate, start, total):
            #output solution
            if target == total:
                res.append(candidate[:])
                return
            if target < total:
                return
            #explore all candidates
            for i in range(start, len(candidates)):
                #check candidate validity
                candidate.append(candidates[i])
                #backtrack
                total += candidates[i]
                backtrack(candidate, i, total)
                #remove
                candidate.pop()
                total -= candidates[i]
                
        backtrack([], 0, 0)
        return res