class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #input: array of nums
        #output: largest sum
        #time complexity O(n) track largest sum, current total if above 0, and new starting total when iterating across
        #space complexity O(1)
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            reset = False
            if num >= curr_sum + num:
                curr_sum = num
            else:
                curr_sum += num
                if curr_sum < 0:
                    curr_sum = 0
                    reset = True
            if not reset:
                max_sum = max(max_sum, curr_sum)
        return max_sum