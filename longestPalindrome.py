class Solution:
    def longestPalindrome(self, s: str) -> str:
        #time complexity O(n^2)
        #space complexity O(n)
        longest_substr = ''
        def insideOut(first_p, second_p):
            nonlocal longest_substr
            if(s[first_p] != s[second_p]):
                return
            while 1:
                if first_p == 0 or second_p == len(s)-1:
                    break
                if s[first_p-1]==s[second_p+1]:
                    first_p -= 1
                    second_p += 1
                else:
                    break
            if second_p+1-first_p > len(longest_substr):
                longest_substr = s[first_p:second_p+1]
            return
        for s_index in range (len(s)):
            insideOut(s_index, s_index)
            if s_index+1 != len(s):
                insideOut(s_index, s_index+1)
        return longest_substr