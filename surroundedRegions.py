class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row, col):
            if row < 0 or row > len(board)-1 or col < 0 or col > len(board[0])-1 or output_board[row][col] == 'O':
                return
            if board[row][col] == 'O':
                output_board[row][col] = 'O'
                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)

        output_board = [['X' for i in range(len(board[0]))] for i in range(len(board))]
        for i in range(max(len(board[0]), len(board))):
            if i < len(board[0]) and board[0][i] == 'O':
                dfs(0, i)
            if i < len(board[0]) and board[len(board)-1][i] == 'O':
                dfs(len(board)-1, i)
            if i < len(board) and board[i][0] == 'O':
                dfs(i, 0)
            if i < len(board) and board[i][len(board[0])-1] == 'O':
                dfs(i, len(board[0])-1)
                
        for row_ind, row in enumerate(board):
            for col_ind, item in enumerate(row):
                board[row_ind][col_ind] = output_board[row_ind][col_ind]