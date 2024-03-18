class Solution:
    def findMinArrowShots(self, points):
        points.sort(key = lambda x: x[1])
        res, end_point = 0, float("-inf")

        for i in points:
            if i[0] > end_point:
                res += 1
                end_point = i[1]

        return res
