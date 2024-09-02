class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #time complexity O(m*n)
        #space complexity O(m*n)
        
        max_area = 0
        curr_area = 0
        visited = set()
        def dfs(row, col):
            nonlocal curr_area
            if row < 0 or row > len(grid)-1 or col < 0 or col > len(grid[0])-1:
                return
            if (row, col) not in visited and grid[row][col] == 1:
                visited.add((row, col))
                curr_area += 1
                dfs(row-1, col)
                dfs(row+1, col)
                dfs(row, col-1)
                dfs(row, col+1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr_area = 0
                if (row,col) not in visited and grid[row][col] == 1:
                    dfs(row, col)
                max_area = max(max_area, curr_area)
        
        return max_area