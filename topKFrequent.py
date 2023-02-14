import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #O(1) time/space complexity
        if k == len(nums):
            return nums
        #time complexity O(n log m)
        #space complexity O(n)
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        rev_freq_dict = {}
        heap = []
        for key, value in freq_dict.items():
            if value not in rev_freq_dict:
                rev_freq_dict[value] = [key]
                heap.append(value)
            else:
                rev_freq_dict[value].append(key)
                heap.append(value)
        heapq.heapify(heap)
        k_most_freq = heapq.nlargest(k, heap)
        ans = []
        for value in k_most_freq:
            ans.append(rev_freq_dict[value].pop())
        return ans