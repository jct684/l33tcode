class Solution:
    def longestPalindrome(self, s: str) -> str:
        #start a pointer at one end and use a second pointer at same letter on opposite end
        #determine if the substring is a palindrome and save length if it is
        #if not substring, bring the pointer in until there are no more duplicate letters
        #repeat across the length of the string
        #if the length of the longest palindrome is greater than the length of the substring then skip
        #time complexity is O(n^2*k) where O(n) is length of string, O(n) is verification, O(k) are duplicates
        #space complexity O(1)
        highest_len = 1
        saved_start = 0
        saved_end = 0
        for i in range(len(s)):
            start = i
            letter = s[i]
            end = s.rfind(letter)
            while start < end:
                if highest_len >= end - start + 1:
                    break
                else:
                    if self.check_palindrome(s[start:end+1]):
                        if end - start + 1 > highest_len:
                            highest_len = end - start + 1
                            saved_start = start
                            saved_end = end
                    end = s.rfind(letter, start, end)
        return s[saved_start:saved_end+1]
    
    def check_palindrome(self, substring):
        start = 0
        end = len(substring)-1
        while start < end:
            if substring[start] != substring[end]:
                return False
            start += 1
            end -= 1
        return True