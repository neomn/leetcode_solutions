class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        diffX, diffY = coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]
        ratio = diffY/diffX if diffX != 0 else float('inf')
        for i in range(1, len(coordinates) - 1): 
