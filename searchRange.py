class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return searchRange(nums, target)

def searchRange(nums, target):
    #binary search modified to search lower values after finding target
    #binary search modified to search higher values after finding target (after finding lower bound)
    #if no target found then return -1
    #time complexity O(log n)
    #space complexity O(1)
    lower_bound = False
    s1_res = binary_search(nums, target, lower_bound)
    if s1_res == -1:
        return [-1, -1]
    else:
        lower_bound = True
    s2_res = binary_search(nums, target, lower_bound)
    return [s1_res, s2_res]
    
    
def binary_search(nums, target, lower_bound):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            if lower_bound is False:
                if mid == 0 or nums[mid-1] < target:
                    return mid
                right = mid - 1
            else:
                if mid  == len(nums)-1 or nums[mid+1] > target:
                    return mid
                left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1