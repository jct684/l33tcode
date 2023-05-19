class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #time complexity O(log n)
        #space complexity O(1)
        first_num = nums[0]
        if(nums[-1] >= nums[0]):
            return binary_search(nums, target, 0, len(nums) - 1)
        low = 0
        high = len(nums) - 1
        while (low + 1 < high):
            index = (low + high) // 2
            if(nums[index] < first_num):
                high = index
            else:
                low = index
        if(target < first_num):
            return binary_search(nums, target, low+1, len(nums) - 1)
        else:
            return binary_search(nums, target, 0, high-1)
        
def binary_search(nums_arr, target, start, end):
    low = start
    high = end
    while(low <= high):
        index = (low + high) // 2
        if(target == nums_arr[index]):
            return index
        if (nums_arr[index] < target):
            low = index + 1
        else:
            high = index - 1
    return -1