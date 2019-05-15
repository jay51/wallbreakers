
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key= lambda x: x[1])
        arrows = 1
        inital = points[0][1]
        
        for start, end in points:
            if start > inital:
                arrows += 1
                inital = end
        return arrows
