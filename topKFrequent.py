import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #time complexity O(n log m)
        #space complexity O(n)
        freq_dict = {}
        for num in nums:
            if (freq_dict.get(num, 0) == 0):
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        rev_freq_dict = {}
        heap = []
        for key, value in freq_dict.items():
            if(rev_freq_dict.get(value, 0) == 0):
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