from typing import List        

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()

        min_x = float("inf")
        min_y = float("inf")
        max_x = float("-inf")
        max_y = float("-inf")

        area = 0

        for x1, y1, x2, y2 in rectangles:

            # Update bounding rectangle
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # Add area
            area += (x2 - x1) * (y2 - y1)

            # Four corners
            points = [
                (x1, y1),
                (x1, y2),
                (x2, y1),
                (x2, y2)
            ]

            # Toggle each corner
            for point in points:
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)

        # Area of the bounding rectangle
        bounding_area = (
            (max_x - min_x) *
            (max_y - min_y)
        )

        # The four outer corners must be the only remaining corners
        expected = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }

        return area == bounding_area and corners == expected