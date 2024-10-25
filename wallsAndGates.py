from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        dq = deque()
        for row, block in enumerate(rooms):
            for col, room in enumerate(block):
                if room == 0:
                    dq.append((row, col, room))
        
        def updateNeighboringRoom(row, col, room):
            if row >= 0 and row < len(rooms) and col >= 0 and col < len(rooms[0]) and rooms[row][col] == 2147483647:
                rooms[row][col] = room+1
                dq.append((row, col, rooms[row][col]))
                
        while dq:
            curr_row, curr_col, curr_room = dq.popleft()
            updateNeighboringRoom(curr_row+1, curr_col, curr_room)
            updateNeighboringRoom(curr_row-1, curr_col, curr_room)
            updateNeighboringRoom(curr_row, curr_col+1, curr_room)
            updateNeighboringRoom(curr_row, curr_col-1, curr_room)
        
        return rooms