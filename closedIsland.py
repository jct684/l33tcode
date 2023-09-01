class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        #time complexity O(m*n)
        #space complexity O(1)
        def edgeDFS():
            for row_index in range (len(grid)):
                for col_index in range (len(grid[0])):
                    if row_index == 0 or row_index == len(grid)-1:
                        DFS(row_index, col_index)
                    elif col_index == 0 or col_index == len(grid[0])-1:
                        DFS(row_index, col_index)
    
        def DFS(row, col):
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] == 1:
                return
            grid[row][col] = 1
            DFS(row+1, col)
            DFS(row-1, col)
            DFS(row, col+1)
            DFS(row, col-1)
        
        edgeDFS()
        count = 0
        for row_index in range (len(grid)):
            for col_index in range (len(grid[0])):
                if grid[row_index][col_index] == 0:
                    count += 1
                    DFS(row_index,col_index)
        return count