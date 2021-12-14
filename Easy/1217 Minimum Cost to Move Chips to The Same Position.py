class Solution:
    def minCostToMoveChips(self, position):
        pos = [0, 0]
        for p in position:
            pos[p & 1] += 1
        return min(pos)
