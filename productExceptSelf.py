class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input: array
        #output: array
        left_arr = [0] * len(nums)
        for index, num in enumerate(nums):
            prev = left_arr[index-1] if index > 0 else 1
            left_arr[index] = num * prev
        right_arr = [0] * len(nums)
        for index, num in reversed(list(enumerate(nums))):
            prev = right_arr[index+1] if index < len(nums)-1 else 1
            right_arr[index] = num * prev
        ans = [0] * len(nums)
        for i in range(len(ans)):
            left = left_arr[i-1] if i > 0 else 1
            right = right_arr[i+1] if i < len(nums)-1 else 1
            ans[i] = left * right
        return ans