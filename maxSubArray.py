class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #I did this problem a long time ago before I knew about dynamic programming
        #I think I should redo this problem in a cleaner way now that I learned it in class
        #OPT(i) = local maximum sum of contiguous subarray
        #OPT(i) = max(nums[i], OPT(i-1) + nums[i])
        #use a tracker to track the global maximum
        #time complexity O(n)
        #space complexity O(n)
        memo = [0 for _ in range(len(nums))]
        global_max = float('-inf')
        for i in range(len(nums)):
            memo[i] = max(nums[i], memo[i-1] + nums[i])
            if (memo[i] > global_max):
                global_max = memo[i]
        return global_max