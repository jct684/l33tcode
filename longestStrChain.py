class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        return longestStrChain(words)

def longestStrChain(words):
    #time complexity O(n*L^2)
    #space complexity O(n)
    memo_dict = {}
    longest_chain = 1
    for word in words:
        longest_chain = max(longest_chain, DFS(word, words, memo_dict))
    return longest_chain

def DFS(word, words, memo_dict):
    if (len(word) == 1):
        memo_dict[word] = 1
        return 1
    elif (word in memo_dict):
        return memo_dict[word]
    else:
        max_length = 1
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            if new_word in words:
                max_length = max(max_length, DFS(new_word, words, memo_dict) + 1)
        memo_dict[word] =  max_length
        return max_length
         
        
        