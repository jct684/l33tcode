from collections import defaultdict
from collections import deque

class Solution:
    def intToRoman(self, num: int) -> str:
        #greedy approach should work
        #find the remainder from the largest possible denomination
        #if the remainder is 4, 40, or 400 then convert symbol to right to next denomination up with the I, X, or C subtracted
        #oops, I made my roman numeral backwards so I added an deque to reverse the order
        num_symbol = defaultdict(lambda :0)
        num_symbol['M'] = num_symbol['M'] + num // 1000
        num = num % 1000
        num_symbol['D'] = num_symbol['D'] + num // 500
        num = num % 500
        num_symbol['C'] = num_symbol['C'] + num // 100
        num = num % 100
        num_symbol['L'] = num_symbol['L'] + num // 50
        num = num % 50
        num_symbol['X'] = num_symbol['X'] + num // 10
        num = num % 10
        num_symbol['V'] = num_symbol['V'] + num // 5
        num = num % 5
        num_symbol['I'] = num_symbol['I'] + num
        ans = deque([])
        if (num_symbol['I'] == 4 and num_symbol['V'] == 1):
            ans.appendleft("IX")
        elif (num_symbol['I'] == 4):
            ans.appendleft("IV")
        else:
            append_to_str(num_symbol, ans, 'I')
            append_to_str(num_symbol, ans, 'V')
        if (num_symbol['X'] == 4 and num_symbol['L'] == 1):
            ans.appendleft("XC")
        elif (num_symbol['X'] == 4):
            ans.appendleft("XL")
        else:
            append_to_str(num_symbol, ans, 'X')
            append_to_str(num_symbol, ans, 'L')
        if (num_symbol['C'] == 4 and num_symbol['D'] == 1):
            ans.appendleft("CM")
        elif (num_symbol['C'] == 4):
            ans.appendleft("CD")
        else:
            append_to_str(num_symbol, ans, 'C')
            append_to_str(num_symbol, ans, 'D')
        append_to_str(num_symbol, ans, 'M')
        return "".join(ans)
            
def append_to_str(num_symbol, ans, key):
    for i in range (num_symbol[key]):
        ans.appendleft(key)
    return ans