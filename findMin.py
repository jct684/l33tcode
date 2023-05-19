class Solution:
    def findMin(self, nums: List[int]) -> int:
        #time complexity O(log n)
        #space complexity O(1)
        if nums[-1] >= nums[0]:
            return nums[0]
        first_num = nums[0]
        low = 0
        high = len(nums) - 1
        while(low + 1 < high):
            index = (low + high) // 2
            if(nums[index] < first_num):
                high = index
            else:
                low = index
        return nums[high]