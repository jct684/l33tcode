class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #check if parenthesis and add to stack to track valid parenthesis
        #stack should track the index and the paren direction
        #if the parenthesis is not valid, then remove from string
        #if parenthesis remain at the end, then remove from string based on index
        #time complexity O(n)
        #space complexity O(number of valid parenthesis stored in stack)
        return min_remove_to_make_valid(s)

def min_remove_to_make_valid(s):
    stack = []
    s = list(s)
    for index in range(len(s)):
        if s[index] == "(":
            stack.append([s[index], index])
        if s[index] == ")":
            if len(stack) == 0:
                s[index] = ""
            else:
                stack.pop()
    while stack:
        index = stack.pop()
        s[index[1]] = ""
    return "".join(s)