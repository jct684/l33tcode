class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #time complexity O(n)
        #space complexity O(n)
        #array of integer cost
        #return the min cost to reach the top floor
        #OPT(i) = min(OPT(i-2)+stair cost, OPT(i-1)+stair cost)
        memo = []
        memo.append(0)
        memo.append(0)
        for stair in range(2, len(cost)+1):
            memo.append(min(memo[stair-2]+cost[stair-2], memo[stair-1]+cost[stair-1]))
        return memo[len(cost)]