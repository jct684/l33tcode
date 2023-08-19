class Solution:
    def rob(self, nums: List[int]) -> int:
        #time complexity O(n)
        #space complexity O(n)
        #OPT(i) = max(OPT(i-1), OPT(i-2) + nums)
        memo = {}
        return robbedMoney(len(nums)-1, nums, memo)

def memoi(f):
    def inner(n, nums, memo):
        if n not in memo:
            memo[n] = f(n, nums, memo)
        return memo[n]
    return inner

@memoi
def robbedMoney(n, nums, memo):
    if n==0:
        return nums[0]
    if n==1:
        return max(nums[0], nums[1])
    return max(robbedMoney(n-1, nums, memo), robbedMoney(n-2, nums, memo)+nums[n])