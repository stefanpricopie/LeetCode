class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best_sell = 0
        
        best_peak = 0

        for elem in prices[::-1]:
            best_peak = elem if elem > best_peak else best_peak

            sell = best_peak - elem

            best_sell = sell if sell > best_sell else best_sell

        return best_sell        

        