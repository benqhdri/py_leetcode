from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        if not prices:
            return ans

        start = prices[0]
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                continue
            else:
                # 要跌了
                ans += prices[i] - start
                start = prices[i + 1]

        ans += prices[-1] - start
        return ans


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
    prices = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(prices))
    prices = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices))
