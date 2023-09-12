class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input: string
        #output: length of longest substring without repeating characters
        #time complexity O(n)
        #space complexity O(n)
        #test 1: "abcdde", 4
        #test 2: "abddcba", 4
        left = 0
        right = 0
        max_length = 0
        members = set()
        while right < len(s):
            while s[right] in members:
                members.remove(s[left])
                left += 1
            members.add(s[right])
            max_length = max(max_length, len(members))
            right += 1
        return max_length