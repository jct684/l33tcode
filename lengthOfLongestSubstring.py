class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        left = 0
        right = 0
        max_count = 0
        membership = {}
        while right < len(s):
            if s[right] not in membership or left > membership[s[right]]:
                membership[s[right]] = right
            else:
                left = membership[s[right]] + 1
                membership[s[right]] = right
            max_count = max(max_count, right-left+1)
            right += 1
        return max_count