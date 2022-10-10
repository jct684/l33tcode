class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #OPT(amount) = num of coins
        #OPT(amount) = OPT(amount-largest compatible currency)+1, if not compatible currency then return -1
        #store values in an array form bottom-up
        #time complexity O(amount * num_coins)
        #space complexity O(amount)
        memo_arr = [float('inf')] * (amount + 1)
        memo_arr[0] = 0
        for coin in coins:
            for sub_amount in range(coin, len(memo_arr)):
                new_amount = sub_amount - coin
                memo_arr[sub_amount] = min(memo_arr[sub_amount], memo_arr[new_amount] + 1)
        if (memo_arr[amount] != float('inf')):
            return memo_arr[amount]
        else:
            return -1