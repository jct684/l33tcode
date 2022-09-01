class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #create a string of parenthesis
        #run two possible recursive functions where add open parenthesis or close parenthesis
        #if number of added open parenthesis is less than n then keep going
        ans = [] 
        generate_parenthesis_recursive(ans, n) #note I don't need to pass in the ans list if its part of the main function but I do in this case because of how leetcode sets up the problem
        return ans

def generate_parenthesis_recursive(ans, n, added_paren= 0, closed_paren= 0, string = []):
    if len(string) == 2*n:
        ans.append("".join(string))
    if added_paren < n:
        string.append("(")
        added_paren += 1
        generate_parenthesis_recursive(ans, n, added_paren, closed_paren, string)
        string.pop()
        added_paren -= 1
    if added_paren > closed_paren:
        string.append(")")
        closed_paren += 1
        generate_parenthesis_recursive(ans, n, added_paren, closed_paren, string)
        string.pop()