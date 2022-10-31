class Solution:
    def rob(self, nums: List[int]) -> int:
        #dynamic programming
        #OPT(i) = maximum money robbed
        #OPT(i) = maximum(OPT(i-2) + nums[i]), OPT(i-1)) where i = index of house robbed
        #time complexity O(n)
        #space complexity O(n)
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            memo = [float('-inf') for _ in range (len(nums))]
            memo[0] = nums[0]
            memo[1] = max(nums[0], nums[1])
            for i in range (2, len(memo)):
                memo[i] = max(memo[i-2] + nums[i], memo[i-1])
            return memo[len(nums)-1]