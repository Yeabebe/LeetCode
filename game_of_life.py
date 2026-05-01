from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        
        directions = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),          (0,1),
            (1,-1),  (1,0),  (1,1)
        ]
        
        # Apply rules with encoding
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        if abs(board[ni][nj]) == 1:
                            live_neighbors += 1
                
                # Live cell
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1  # dies
                
                # Dead cell
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2  # becomes alive
        
        # Finalize state
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0