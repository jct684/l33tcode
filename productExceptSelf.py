class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create left/right array O(n) time complexity, O(n) space complexity
        left_array = [1]
        for i in range (1, len(nums)):
            left_array.append(left_array[i-1] * nums[i-1])
        right_array = [1]
        for i in range (1, len(nums)):
            right_array.append(right_array[i-1] * nums[len(nums)-i])
        right_array.reverse()
        ans = []
        for i in range (len(nums)):
            ans.append(left_array[i] * right_array[i])
        return ans