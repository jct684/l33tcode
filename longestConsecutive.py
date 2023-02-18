class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #O(n) time complexity
        #O(n) space complexity
        num_set = set(nums)
        max_consec = 0
        for num in num_set:
            if num-1 not in num_set:
                curr_consec = 1
                while num+1 in num_set:
                    curr_consec += 1
                    num += 1
                max_consec = max(max_consec, curr_consec)
        return max_consec