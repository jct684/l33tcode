class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #O(1) time/space complexity
        if k == len(nums):
            return nums
        #time complexity O(n)
        #space complexity O(n)
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        freq_array = [None for _ in range(len(nums)+1)]
        for key, value in freq_dict.items():
            if freq_array[value] == None:
                freq_array[value] = [key]
            else:
                freq_array[value].append(key)
        k_count = 0
        ans = []
        while k_count < k:
            temp = freq_array.pop()
            if temp != None:
                for _ in range(len(temp)):
                    ans.append(temp.pop())
                    k_count += 1
        return ans