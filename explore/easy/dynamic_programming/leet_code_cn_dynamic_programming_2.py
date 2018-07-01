# 解题思路：算出最后几个数字的最大值，然后和前面的那个数字比较，保留最大值
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max_profit = 0  # 从后向前的最大收益
        max_price = 0  # 当前计算数组中的最高价格
        for i in range(len(prices) - 1, 0, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            if max_price - prices[i - 1] > max_profit:
                max_profit = max_price - prices[i - 1]

        return max_profit


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProfit([7, 6, 4, 3, 1])
    print(result)
