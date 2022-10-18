class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #OPT(i, buy/sell) = maximum profit by buying/selling at day i
        #OPT(i, buy) = max(OPT(i-1, buy), OPT(i-1, sell) - prices[i] - fee)
        #when you are buying, you either held previous buy or sold previous step and are buying again
        #OPT(i, sell) = max(OPT(i-1, sell), OPT(i-1, buy) + prices[i])
        #when you are selling, you either bought/held previously or are buying and cannot sell
        #time complexity O(n)
        #space complexity O(n)
        #space complexity could be reduced since we only really need the previous index
        memo = [[float('-inf'), float('-inf')] for _ in range (len(prices))]
        memo[0][0] = -prices[0] - fee
        memo[0][1] = 0
        for i in range (1, len(memo)):
            memo[i][0] = max(memo[i-1][0], memo[i-1][1] - prices[i] - fee)
            memo[i][1] = max(memo[i-1][1], memo[i-1][0] + prices[i])
        return memo[len(prices)-1][1]