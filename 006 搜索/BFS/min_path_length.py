from queue import Queue
from typing import List

DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def min_path_length(grids: List[List[int]], tr: int, tc: int):
    """求解从（0，0）到（tr，tc）的最短距离"""

    def not_satisfied(node):
        return node[0] < 0 or node[0] >= m \
               or node[1] < 0 or node[1] >= n \
               or grids[node[0]][node[1]] == 0

    m, n = len(grids), len(grids[0])

    queue = Queue()
    queue.put([0, 0])
    path_length = 0
    while queue.not_empty:
        size = queue.qsize()
        path_length += 1
        for _ in range(size):
            cur = queue.get()
            for d in DIRECTIONS:
                next_node = [cur[0] + d[0], cur[1] + d[1]]
                if not_satisfied(next_node):
                    continue

                grids[next_node[0]][next_node[1]] = 0
                if next_node[0] == tr and next_node[1] == tc:
                    return path_length

                queue.put(next_node)

    return -1


if __name__ == '__main__':
    print(min_path_length([[1, 1, 0, 1],
                           [1, 0, 1, 0],
                           [1, 1, 1, 1],
                           [1, 0, 1, 1]], 1, 2))
