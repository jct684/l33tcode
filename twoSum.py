class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #input: indexed array sorted in non-decreasing order
        #output: two indicies +1 in an array
        #constant extra space
        #TEST: [-4, -2, 0, 0, 3, 4] target: 1, ANS: [2, 6]
        left_ind = 0
        right_ind = len(numbers)-1
        total = numbers[0] + numbers[-1]
        while total != target:
            if total < target:
                left_ind += 1
            else:
                right_ind -= 1
            total = numbers[left_ind] + numbers[right_ind]
        return [left_ind+1, right_ind+1]