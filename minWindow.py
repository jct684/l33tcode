class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #time complexity O(n + m) where n is length of s string and m is length of t string
        #space complexity O(n + m)
        t_dict = {}
        s_dict = {}
        t_len = 0
        for letter in t:
            t_len += 1
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1
                s_dict[letter] = 0
        s_len = 0
        first_p = 0
        second_p = first_p
        max_substr = ""
        substr_len = float('inf')
        while second_p < len(s):
            if s[second_p] in s_dict:
                if s_dict[s[second_p]] < t_dict[s[second_p]]:
                    s_len += 1
                s_dict[s[second_p]] += 1
                while(s_len == t_len):
                    if (substr_len > second_p + 1 - first_p):
                        max_substr = s[first_p:second_p+1]
                        substr_len = second_p + 1 - first_p
                    if s[first_p] in s_dict:
                        s_dict[s[first_p]] -= 1
                        if s_dict[s[first_p]]  < t_dict[s[first_p]]:
                            s_len -= 1
                    first_p += 1
            second_p += 1
        return max_substr