from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #time complexity O(n)
        #space complexity O(n)
        max_len = 0
        left = 0
        right = 0
        max_dq = deque()
        min_dq = deque()
        while right < len(nums):
            while max_dq and max_dq[-1] < nums[right]:
                max_dq.pop()
            max_dq.append(nums[right])
            while min_dq and min_dq[-1] > nums[right]:
                min_dq.pop()
            min_dq.append(nums[right])
            
            while max_dq[0] - min_dq[0] > limit:
                if max_dq[0] == nums[left]:
                    max_dq.popleft()
                if min_dq[0] == nums[left]:
                    min_dq.popleft()
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
                