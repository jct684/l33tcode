class Solution:
    def maxArea(self, height: List[int]) -> int:
        #first pointer at start
        #second pointer at end
        #move inward from shorter pointer
        #if tie, doesn't matter which pointer moves as the max area would still be greater unless a higher height is found
        #time complexity O(n)
        #space complexity O(1)
        return maxArea(height)

def maxArea(height):
    start = 0
    end = len(height)-1
    ans = 0
    while (start < end):
        if  (height[start] < height[end]):
            ans = max(ans, height[start] * (end-start))
            start += 1
        else:
            ans = max(ans, height[end] * (end-start))
            end -= 1
    return ans
        