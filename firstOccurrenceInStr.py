class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #time complexity O(n*m)
        #space complexity O(1) 
        for i in range (len(haystack) - len(needle)+1):
            if(haystack[i] == needle[0]):
                if(window(haystack, needle, i)):
                   return i
        return -1
            
def window(haystack_substr, needle_str, haystack_index):
    for i in range (len(needle_str)):
        if needle_str[i] != haystack_substr[haystack_index + i]:
            return False
    return True