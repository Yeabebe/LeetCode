from typing import List     

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    
                    # If there is an X above or to the left,
                    # this X belongs to an existing battleship.
                    if r > 0 and board[r - 1][c] == 'X':
                        continue
                    
                    if c > 0 and board[r][c - 1] == 'X':
                        continue
                    
                    # No X above or left -> start of a battleship
                    count += 1

        return count