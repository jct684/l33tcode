class Solution:
    def trap(self, height: List[int]) -> int:
        #time complexity O(n)
        #space complexity O(1)
        left = 0
        right = len(height)-1
        max_left = 0
        max_right = 0
        trap_area = 0
        while left < right:
            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                trap_area += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                trap_area += max_right - height[right]
                right -= 1
        return trap_area