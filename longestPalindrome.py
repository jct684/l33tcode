class Solution:
    def longestPalindrome(self, s: str) -> str:
        #inside out approach for determining palindrome
        #time complexity O(n^2), O(n) to iterate through list, O(n) to determine outward expansion
        #space complexity O(1)
        self.highest_len = 0
        self.start = 0
        self.end = 1
        for i in range(len(s)-1):
            self.expand_outward(s, i, i)
            self.expand_outward(s, i, i+1)
        return s[self.start:self.end]
            
    def expand_outward(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if self.highest_len < right - left + 1:
            self.highest_len = right - left + 1
            self.start = left+1
            self.end = right