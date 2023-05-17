class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #time complexity O(n)
        #space complexity O(n)
        str_set = set()
        first_p = 0
        second_p = 0
        longest_sub = 0
        for letter in s:
            if letter not in str_set:
                str_set.add(s[second_p])
                second_p += 1
                longest_sub = max(longest_sub, second_p - first_p)
            else:
                while(s[first_p] != s[second_p]):
                    str_set.remove(s[first_p])
                    first_p += 1
                first_p += 1
                second_p += 1
        return longest_sub