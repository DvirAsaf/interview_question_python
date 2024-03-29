"""
939. Minimum Area Rectangle
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points,
with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.
"""
from typing import List


def min_area_rect(self, points: List[List[int]]) -> int:
    res = float('inf')
    pts = set([(x, y) for x, y in points])

    for x1, y1 in points:
        for x2, y2 in points:
            """
            our goal is to find two points that are diagonal to each 
            other, therefore we want to check that for (x1, y1) and (x2,
            y2) either x1 < x2 AND y1 < y2 or the other way around.
            """
            if x1 < x2 and y1 < y2:
                # now checking that there are actually all 4 points of the
                # rectangle in the set
                if (x1, y2) in pts and (x2, y1) in pts:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    res = min(res, area)
    if res == float('inf'):
        return 0
    return res
