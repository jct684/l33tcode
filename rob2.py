class Solution:
    def rob(self, nums: List[int]) -> int:
        #time complexity O(n)
        #space complexity O(n)
        first_memo_h = {}
        second_memo_h = {}
        if len(nums) == 1:
            return nums[0]
        return max(robHouse(len(nums)-2, nums[:len(nums)-1], first_memo_h), robHouse(len(nums)-2, nums[1:len(nums)], second_memo_h))

def memoi(f):
    def inner(n, nums, memo):
        if n not in memo:
            memo[n] = f(n, nums, memo)
        return memo[n]
    return inner

@memoi
def robHouse(n, nums, memo):
    if n==0:
        return nums[0]
    elif n==1:
        return max(nums[0], nums[1])
    return max(robHouse(n-2, nums, memo) + nums[n], robHouse(n-1, nums, memo))