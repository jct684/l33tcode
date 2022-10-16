class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dynamic programming solution
        #OPT(i) = maximum profit achieved where i is the first day you can buy
        #OPT(i) = max(OPT(n-i), profit of selling at current day compared to buying previous days)
        #time complexity O(n)
        #space complexity O(n)
        #OPT(n-1) = 0
        n = len(prices)
        memo = [0 for _ in range (n + 1)]
        memo[n] = 0
        highest_num = prices[n-1]
        for i in range (n - 1, 0, -1):
            memo[i] = max(memo[i+1], highest_num - prices[i-1])
            highest_num = max(highest_num, prices[i-1])
        return memo[1]