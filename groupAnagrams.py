class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input: array of strings
        #return: array of arrays including grouped anagrams
        ana_dict = {}
        for word in strs:
            word_list = ana_dict.get(str(sorted(word)), [])
            word_list.append(word)
            ana_dict[str(sorted(word))] = word_list
        return ana_dict.values()