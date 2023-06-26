class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, col, index, path):
            if(index == len(word)):
                return True
            if(row < 0 or col < 0 or row == len(board) or col == len(board[0]) or (row, col) in path):
                return False
            if(board[row][col] != word[index]):
                return False
            index += 1
            path.add((row, col))
            up = dfs(row-1, col, index, path)
            down = dfs(row+1, col, index, path)
            left = dfs(row, col-1, index, path)
            right = dfs(row, col+1, index, path)
            path.remove((row, col))
            return up or down or left or right
        
        for start_row in range(len(board)):
            for start_col in range(len(board[0])):
                if(board[start_row][start_col] == word[0]):
                    index = 0
                    path = set()
                    if dfs(start_row, start_col, index, path):
                        return True
        return False