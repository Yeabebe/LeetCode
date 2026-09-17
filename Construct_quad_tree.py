from typing import List, Node      

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def build(r, c, size):
            # Check if the current square is uniform
            value = grid[r][c]
            same = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != value:
                        same = False
                        break
                if not same:
                    break

            # If all values are the same, create a leaf
            if same:
                return Node(value == 1, True, None, None, None, None)

            half = size // 2

            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)

            return Node(
                True,
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )

        return build(0, 0, len(grid))