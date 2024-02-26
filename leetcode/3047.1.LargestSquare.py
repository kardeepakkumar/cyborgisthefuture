class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        side = 0
        for r1 in range(0, n-1):
            for r2 in range(r1+1, n):
                x1 = max(bottomLeft[r1][0], bottomLeft[r2][0])
                x2 = min(topRight[r1][0], topRight[r2][0])
                y1 = max(bottomLeft[r1][1], bottomLeft[r2][1])
                y2 = min(topRight[r1][1], topRight[r2][1])
                side = max(side, min(x2-x1, y2-y1))
        return side*side

# metadata
# relevant-topics geometry, 2d array
# time-complexity O(N^2) 50.00%
# space-complexity O(1) 100.00%
# language python
# difficulty easy
# date 20240225