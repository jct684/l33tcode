from random import randint 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick select implementation
        #place the pivot in the correct index along with smaller/larger numbers on opposite sides
        #if the pivot is in the k-1 spot then return the pivot
        #if the pivot is not in the k-1 spot then check if higher or lower before repeating above-mentioned steps
        #O(n) average but O(n^2) worst case
        #O(1) space complexity
        #consider using a random number generator to select the pivot randomly
        return findKthLargest(nums, k)

def findKthLargest(nums, k):
    left = 0
    right = len(nums)
    return quick_select(nums, k, left, right)


def partition(nums, left, right, pivot_index):
    nums[pivot_index], nums[-1] = nums[-1], nums[pivot_index]
    pivot_index = len(nums)-1
    stored_index = left
    for i in range(left, right):
        if nums[i] < nums[pivot_index]:
            nums[stored_index], nums[i] = nums[i], nums[stored_index]
            stored_index += 1
    nums[stored_index], nums[pivot_index] =  nums[pivot_index], nums[stored_index]
    return stored_index

def quick_select(nums, k, left, right):
    if left == right:
        return nums[len(nums)-k]
    pivot_index = randint(left, right-1)
    pivot_index = partition(nums, left, right, pivot_index)
    if pivot_index == len(nums)-k:
        return nums[pivot_index]
    
    if pivot_index < len(nums)-k:
        left = pivot_index + 1
        return quick_select(nums, k, left, right)
    
    if pivot_index > len(nums)-k:
        right = pivot_index
        return quick_select(nums, k, left, right)