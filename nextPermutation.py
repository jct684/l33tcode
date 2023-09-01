class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #time complexity O(n)
        #space complexity O(1)
        index = len(nums)-2
        while index >= 0 and nums[index+1] <= nums[index]:
            index -= 1
        if index >= 0:
            swap_index = len(nums)-1
            while nums[index] >= nums[swap_index]:
                swap_index -= 1
            nums[index], nums[swap_index] = nums[swap_index], nums[index]
        nums[index+1:len(nums)] = nums[index+1:len(nums)][::-1]
        return nums