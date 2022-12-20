class Solution:
    def climbStairs(self, n: int) -> int:
        #dynamic programming solution
        #OPT(i) = number of ways to climb to the top
        #OPT(0) = 0, OPT(1) = 1, OPT(2) = 2
        #OPT(i) = OPT(i-1) + OPT(i-2)
        #all the ways you got to 2 steps ago (add +2 step) and all the ways you got to 1 step ago (add 1 step)
        #time complexity O(n)
        #space complexity O(n)
        memo = []
        memo.append(0)
        memo.append(1)
        memo.append(2)
        for i in range (3, n+1):
            memo.append(memo[i-1] + memo[i-2])
        return memo[n]