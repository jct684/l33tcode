class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #O(m*n log n) time complexity
        #O(m*n) space complexity
        ana_dict = {}
        for index in range (len(strs)):
            word_sort = str(sorted(strs[index]))
            if word_sort in ana_dict:
                ana_dict[word_sort].append(strs[index])
            else:
                ana_dict[word_sort] = [strs[index]]
        ans = [val for val in ana_dict.values()]
        return ans