from typing import List

DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def min_path_length(grids: List[List[int]], tr: int, tc: int):
    """求解从（0，0）到（tr，tc）的最短距离"""
    m, n = len(grids), len(grids[0])

    q = [[0, 0]]
    path_length = 0
    while q:
        path_length += 1
        for _ in range(len(q)):
            i, j = q.pop()
            for d1, d2 in DIRECTIONS:
                ni, nj = i + d1, j + d2
                if ni < 0 or ni >= m or nj < 0 or nj >= n or grids[ni][nj] == 0:
                    continue

                grids[ni][nj] = 0
                if ni == tr and nj == tc:
                    return path_length

                q.append([ni, nj])
    return -1
