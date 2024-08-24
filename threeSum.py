class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #time complexity O(n^2)
        #space complexity O(n)
        res = []
        nums.sort()
        
        def validTwoSum(nums, target):
            left = 0
            right = len(nums)-1
            while left < right: 
                if (nums[left] + nums[right] + target) != 0:
                    if nums[right] > (-target - nums[left]):
                        right -= 1
                    else:
                        left += 1
                else:
                    res.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        index = 0
        while nums[index] <= 0 and index < len(nums)-2:
            if index == 0 or nums[index] != nums[index-1]:
                validTwoSum(nums[index+1:],nums[index])
            index += 1
        return res