from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        cnt = 1
        for i in range(1, len(points)):
            if points[i][0] <= points[i - 1][1]:
                # 区间重叠
                points[i][1] = points[i - 1][1]
            else:
                # 区间不重叠
                cnt += 1

        return cnt


"""
if __name__ == '__main__':
    print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
    print(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
    print(Solution().findMinArrowShots([[1, 2]]))
    print(Solution().findMinArrowShots([[2, 3], [2, 3]]))
"""
