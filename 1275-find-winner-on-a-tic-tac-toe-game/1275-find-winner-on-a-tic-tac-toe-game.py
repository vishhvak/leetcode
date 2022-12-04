import numpy as np
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        N = 3
        
        def create_board():
            board = [[None, None, None] for i in range(0, N)]
            for i in range(0, len(moves)):
                if i % 2 == 0:
                    board[moves[i][0]][moves[i][1]] = 'X'
                else:
                    board[moves[i][0]][moves[i][1]] = 'O'
            return board
        
        
        board = create_board()
        
        def check_row(row):
            return len(set(row)) == 1
        
        def row_win(board):
            for i in range(0, len(board)):
                row = board[i]
                if check_row(row):
                    return row[0]
            return False
            
        def check_diag():
            diag1 = []
            diag2 = []
            for i in range(0, N):
                diag1.append(board[i][i])
                diag2.append(board[i][N-1-i])
            if check_row(diag1):
                return diag1[0]
            if check_row(diag2):
                return diag2[0]
            return False
        
        def board_full():
            for i in range(0, N):
                for j in range(0, N):
                    if board[i][j] is None:
                        return False
            return True
        
        row_cond = row_win(board)
        col_cond = row_win(np.array(board).T.tolist())
        diag_cond = check_diag()
        player_map = {'X':'A', 'O':'B'}
        if(row_cond):
            return player_map[row_cond]
        if(col_cond):
            return player_map[col_cond]
        if(diag_cond):
            return player_map[diag_cond]
        if(board_full()):
            return 'Draw'
        return 'Pending'