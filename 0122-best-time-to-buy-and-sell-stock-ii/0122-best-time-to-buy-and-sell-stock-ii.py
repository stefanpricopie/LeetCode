class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # corner case len(prices)=0
        if not prices:
            return 0

        last_low = prices[0]
        profit = 0

        for i, price in enumerate(prices[1:]):

            prev_price = prices[i]

            if prev_price > price:
                profit += prev_price - last_low
                last_low = price
        
        profit += prices[-1] - last_low

        return profit