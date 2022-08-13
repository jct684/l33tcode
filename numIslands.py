class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS to find all connected 1's to determine an island
        #time complexity O(row*column)
        #space complexity O(number of lands)
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.DFS(grid,i,j)
        return num_islands

    def DFS(self, grid, row, col):
        if row > len(grid)-1 or row < 0 or col > len(grid[row])-1 or col < 0 or grid[row][col] == "0":
            pass
        else:
            grid[row][col] = "0"
            self.DFS(grid, row, col+1)
            self.DFS(grid, row+1, col)
            self.DFS(grid, row-1, col)
            self.DFS(grid, row, col-1)