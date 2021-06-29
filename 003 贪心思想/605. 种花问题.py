from typing import List


def check_ok(flowerbed, i):
    pre, after = i - 1, i + 1
    return (pre < 0 or flowerbed[pre] == 0) and \
           (after >= len(flowerbed) or flowerbed[after] == 0)


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i, planted in enumerate(flowerbed):
            if n <= 0:
                break

            if not planted and check_ok(flowerbed, i):
                n -= 1
                flowerbed[i] = 1

        return n <= 0
