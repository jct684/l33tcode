class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #time complexity O(n)
        #space complexity O(n)
        if len(s) < 10:
            return []
        res = set()
        seen = set()
        left = 0
        right = 9
        while right < len(s):
            seq = s[left:right+1]
            if seq in seen:
                res.add(seq)
            else:
                seen.add(s[left:right+1])
            left += 1
            right += 1
        return [item for item in res]
        