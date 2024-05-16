class Solution:
    def maxArea(self, height: List[int]) -> int:
        #input: height array
        #output: max volume of water
        #TEST: [0, 1, 7, 2, 7, 2], ANS: 21
        #time complexity O(n), space complexity O(1)
        left = 0
        right = len(height)-1
        max_vol = 0
        while left < right:
            max_vol = max(max_vol, min(height[left], height[right])*(right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_vol