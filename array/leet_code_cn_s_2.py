class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        buy_price = prices[0]
        is_hold = False
        money = 0
        for index in range(1, len(prices)):
            if prices[index] < prices[index - 1] and is_hold:
                money = money + (prices[index - 1] - buy_price)
                is_hold = False
            elif prices[index] > prices[index - 1] and not is_hold:
                buy_price = prices[index - 1]
                is_hold = True
            if index + 1 == len(prices) and is_hold:
                money = money + prices[index] - buy_price

        return money


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProfit(prices=[7,1,5,3,6,4])
    print(result)
