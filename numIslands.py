import copy
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #time complexity O(row * col)
        #space complexity O(row * col)
        count = 0
        copyIslands = copy.deepcopy(grid)
        def dfs(row, col):
            if row<0 or col<0 or row==len(grid) or col == len(grid[0]) or copyIslands[row][col] == '0':
                return
            if copyIslands[row][col] == '1':
                copyIslands[row][col] = '0'
                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if copyIslands[row][col] == '1':
                    count += 1
                    dfs(row, col)
        return count