class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        total = 0
        curr_list = []
        index = 0
        def dfs(index, curr_list, total):
            if total == target:
                res.append(curr_list.copy())
                return
            if index == len(candidates) or total > target:
                return
            curr_list.append(candidates[index])
            dfs(index, curr_list, total + candidates[index])
            curr_list.pop()
            dfs(index+1, curr_list, total)
        dfs(index, curr_list, total)
        return res