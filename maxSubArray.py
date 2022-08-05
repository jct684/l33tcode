class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #start at the first positive number as largest sum
        #find sum of subsequent number and store higher value
        #if the sum is zero or lower then reset at next number
        #if number is above zero, then continue to store max of next sum
        #continue until end of array
        #check again at end of array for max
        i = 0
        large_sum = nums[i]
        larger = 0
        positive_number = False
        while i < len(nums) and nums[i]<=0:
            large_sum = max(nums[i], large_sum)
            i += 1
        while i < len(nums):
            if larger <= 0:
                larger = 0
            if nums[i] >= 0:
                larger += nums[i]
                i += 1
            else:
                large_sum = max(large_sum, larger)
                larger += nums[i]
                i += 1
        if nums[i-1] >= 0:
            large_sum = max(large_sum, larger)
        return large_sum
