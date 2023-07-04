class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #time complexity O(m*n)
        #space complexity O(m*n)
        atlantic_set = set()
        pacific_set = set()
        res = []

        def dfs(visited_set, row, col, prev):
            if(row < 0 or col < 0 or row == len(heights) or col == len(heights[0]) or prev > heights[row][col]):
                return
            if (row, col) in visited_set:
                return
            else:
                visited_set.add((row,col))
            prev = heights[row][col]
            dfs(visited_set, row+1, col, prev)
            dfs(visited_set, row-1, col, prev)
            dfs(visited_set, row, col+1, prev)
            dfs(visited_set, row, col-1, prev)
        
        for col in range (len(heights[0])):
            dfs(pacific_set, 0, col, heights[0][col])
            dfs(atlantic_set, len(heights)-1, col, heights[len(heights)-1][col])
        for row in range(len(heights)):
            dfs(pacific_set, row, 0, heights[row][0])
            dfs(atlantic_set, row, len(heights[0])-1, heights[row][len(heights[0])-1])
        for (row, col) in atlantic_set:
            if (row, col) in pacific_set:
                res.append([row, col])
                
        return res