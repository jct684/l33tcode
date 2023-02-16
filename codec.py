class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        str_final = ""
        for string in strs:
            str_length = len(string)
            str_delimiter = chr(278)
            str_final += str(str_length) + str_delimiter + string
        return str_final
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        index = 0
        ans = []
        prev_index = 0
        while(index < len(s)):
            if(s[index] == chr(278)):
                str_length = int(s[prev_index:index])
                ans.append(s[index+1:index+str_length+1])
                prev_index = index+str_length+1
            index += 1
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))