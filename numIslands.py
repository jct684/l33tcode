class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS to find all connected 1's to determine an island
        #time complexity O(row*column)
        #space complexity O(number of lands)
        num_islands = 0
        visited = {}
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if visited.get((row, col), False):
                    continue
                if grid[row][col] == "1":
                    num_islands += 1
                    DFS(grid, row, col, visited)
        return num_islands

def DFS(grid, row, col, visited):
    if not(row > len(grid)-1 or row < 0 or col > len(grid[row])-1 or col < 0 or grid[row][col] == "0" or visited.get(tuple([row, col]))):
        visited[(row,col)] = True
        DFS(grid, row, col+1, visited)
        DFS(grid, row+1, col, visited)
        DFS(grid, row-1, col, visited)
        DFS(grid, row, col-1, visited)