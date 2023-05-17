class Solution:
    #time complexity O(n^2)
    #space complexity O(1), O(n) including answer
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        anchor_p = 0
        first_p = anchor_p + 1
        second_p = len(nums) - 1
        output = []
        while (anchor_p < len(nums)-1 and nums[anchor_p] < 1 and second_p > first_p):
            total = nums[anchor_p] + nums[first_p] + nums[second_p]
            if (total > 0):
                second_p -= 1
            elif (total < 0):
                first_p += 1
            else:
                output.append([nums[anchor_p], nums[first_p], nums[second_p]])
                second_p -= 1
                first_p += 1
                while(second_p > first_p and nums[first_p - 1] == nums[first_p] and nums[second_p + 1] == nums[second_p]):
                    second_p -= 1
                    first_p += 1
            if(second_p <= first_p):
                anchor_p += 1
                while(anchor_p < len(nums) and nums[anchor_p] == nums[anchor_p-1]):
                    anchor_p += 1
                first_p = anchor_p + 1
                second_p = len(nums) - 1
        return output