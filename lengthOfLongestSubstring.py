class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #naive solution: start at every character and iterate across string until find repeat
        #take maximun count for each string starting at every character O(n^3), O(n^2 (create substrings)*n (check duplicates))
        #another solution: use a sliding window with dictionary to store indices O(n) timecomplexity
        i = 0
        index_dict = {}
        longest_substring = 0
        for j in range (len(s)):
            if s[j] not in index_dict:
                index_dict.update({s[j]: j})
            elif s[j] in index_dict:
                if index_dict.get(s[j]) >= i:
                    i  = index_dict.get(s[j])+1
                index_dict.update({s[j]: j}) 
            longest_substring = max(j-i+1, longest_substring)
        return longest_substring