class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #hashmap containing mapping for numbers to letters
        #backtrack problem
        #time complexity: O(n * 4^n)
        #space complexity: O(n)
        mapping = {"2":["a", "b", "c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j", "k", "l"], "6":["m","n","o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        if len(digits) == 0:
            return []
        res = []
        backtrack(0, [], res, digits, mapping)
        return res

def backtrack(index, path, res, digits, mapping):
    if len(path) == len(digits):
        res.append("".join(path))
        return 
    
    new_letters = mapping[digits[index]]
    for letter in new_letters:
        path.append(letter)
        backtrack(index + 1, path, res, digits, mapping)
        path.pop()