class Solution:
    def reorganizeString(self, s: str) -> str:
        #time complexity O(n)
        #space complexity O(k) k is number of unique letters in s
        char_counter = {}
        max_char = None
        max_char_count = 0
        for letter in s:
            char_counter[letter] = char_counter.get(letter, 0) + 1
            if char_counter[letter] > max_char_count:
                max_char_count = char_counter[letter]
                max_char = letter

        if max_char_count > (len(s)+1) // 2:
            return ""
        res = [''] * len(s)
        i = 0
        while char_counter[max_char] > 0:
            res[i] = max_char
            char_counter[max_char] -= 1
            i += 2
        for letter, count in char_counter.items():
            while char_counter[letter] > 0:
                if i > len(res)-1:
                    i = 1
                res[i] = letter
                char_counter[letter] -= 1
                i += 2
        return "".join(res)