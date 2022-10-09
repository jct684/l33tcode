from collections import defaultdict

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #return a value that is the maximum length of a subarray in both arrays
        #check right-to-left each number in nums1 against a corresponding number in nums2
        #OPT(i, j) = 1 if OPT(i+1, j+1) is not initialized
        #otherwise, OPT(i, j) = OPT(i+1, j+1) + 1
        #time complexity O(n*m) check n numbers against size m array
        #space complexity O(n*m) n calls with size m arrays
        memo_dict = defaultdict(lambda :0)
        for i in range (len(nums1) - 1, -1, -1):
            for j in range (len(nums2) - 1, -1, -1):
                if (nums1[i] == nums2[j]):
                    curr_tuple = (i, j)
                    next_tuple = (i+1, j+1)
                    memo_dict[curr_tuple] = memo_dict[next_tuple] + 1
        max_length = 0
        for v in memo_dict.values():
            max_length = max(max_length, v)
        return max_length