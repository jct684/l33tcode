class Solution:
    def longestPalindrome(self, s: str) -> str:
        #inside out approach for determining palindrome
        #time complexity O(n^2), O(n) to iterate through list, O(n) to determine outward expansion
        #space complexity O(k) where k is length of substring
        #to improve space complexity, we could probably just return the left and right ends and then return the sliced string s
        highest_len = 0
        substring_saved = s[0]
        for i in range(len(s)-1):
            substring_1 = self.expand_outward(s, i, i)
            substring_2 = self.expand_outward(s, i, i+1)
            if len(substring_1) > highest_len:
                highest_len = len(substring_1)
                substring_saved = substring_1
            if len(substring_2) > highest_len:
                highest_len = len(substring_2)
                substring_saved = substring_2
        return substring_saved
            
    def expand_outward(self, s, left, right):
        substring = s[left]
        expand = False
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            expand = True
        if expand:
            substring = s[left+1:right]
        return substring