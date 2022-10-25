class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #time complexity O(n)
        #space complexity O(1)
        first_p = 1
        for i in range(1, len(nums)):
            if (nums[i] != nums[i-1]):
                nums[first_p] = nums[i]
                first_p += 1
        return first_p