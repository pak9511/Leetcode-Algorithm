class Solution:
    def findMinArrowShots(self, points):
        n = len(points)
        if n<2:
            return n

        START, END = 0,1
        points.sort(key=lambda i: i[0])
        prev = points[0]
        arrows = 0
        
        for cur in points[1:]:
            if cur[START] <= prev[END]:
                prev = [cur[START], min(cur[END],prev[END])]
            else:
                arrows += 1
                prev = cur

        return arrows+1
