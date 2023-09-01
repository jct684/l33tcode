class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #time complexity O(n * 2^n) 2 copies of array across entire array
        #space complexity O(n)
        path = []
        start = 0
        ans = []
        def backtrack(start, path):
            ans.append(list(path))
            for i in range (start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(start, path)
        return ans