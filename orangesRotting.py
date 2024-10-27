from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def rotOranges(row, col, minute):
            nonlocal orange_count
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1:
                dq.append((row, col, minute+1))
                grid[row][col] = 2
                orange_count -= 1
            
        orange_count = 0
        dq = deque()
        for row, row_orngs in enumerate(grid):
            for col, org in enumerate(row_orngs):
                if org == 2:
                    dq.append((row, col, 0))
                elif org == 1:
                    orange_count += 1
        
        highest_minute = 0
        while dq:
            row, col, minute = dq.popleft()
            rotOranges(row-1, col, minute)
            rotOranges(row+1, col, minute)
            rotOranges(row, col-1, minute)
            rotOranges(row, col+1, minute)
            highest_minute = max(highest_minute, minute)
        
        
        if orange_count == 0:
            return highest_minute
        return -1