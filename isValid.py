class Solution:
    def isValid(self, s: str) -> bool:
        #time complexity O(n)
        #space complexity O(n)
        stack = []
        match_dict = {'(':')', '[': ']', '{':'}'}
        for char in s:
            if char in match_dict:
                stack.append(char)
            elif char == ')' or char == ']' or char == '}':
                if len(stack) == 0:
                    return False
                if char != match_dict[stack.pop()]:
                    return False
        if len(stack) > 0:
            return False
        return True