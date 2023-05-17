class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #time complexity O(n)
        #space complexity O(1)
        first_p = 0
        second_p = first_p
        freq_dict = {}
        max_length = 0
        max_freq = 1
        while (second_p < len(s)):
            if s[second_p] in freq_dict:
                freq_dict[s[second_p]] += 1
                if freq_dict[s[second_p]] > max_freq:
                    max_freq = freq_dict[s[second_p]]
            else:
                freq_dict[s[second_p]] = 1
            while((second_p + 1 - first_p - max_freq) > k):
                freq_dict[s[first_p]] -= 1
                first_p += 1
                #max_freq = 0
                #for v in freq_dict.values():
                    #max_freq = max(max_freq, v)
            second_p += 1
            max_length = max(max_length, second_p - first_p)
        return max_length